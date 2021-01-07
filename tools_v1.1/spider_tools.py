#encoding:utf-8
from bs4 import BeautifulSoup
import json
import requests
import pymysql
import pandas as pd
import re
import urllib3


class Getweb_tools():
    """
    请求获取WEB HTML 代码快捷合集

    """
    def __init__(self):
        pass

    def error_reminder(self,ex):
        print("*****************************************************************************")
        print("")
        print("")
        print(f"程序报错提示：{ex}")
        print("")
        print("")
        print("*****************************************************************************")

    def html_get(self,url, headers,ipagent=None):
        """
        html 的 bs4 解析请求网页

        :param url:请求的url地址
        :param headers:请求头部
        :param ipagent:IP代理

        :return:
        """
        """
        update log:
        1.2021年1月2日03:10:40 -- 增加了更强的编码识别
        
    
        """
        try:
            response = requests.get(url, headers=headers, timeout=10,proxies=ipagent)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

            chardet_text = response.apparent_encoding

            if chardet_text == "GB2312" or chardet_text == "gb2312":
                return BeautifulSoup(response.content, 'lxml', from_encoding="gb18030")

            if chardet_text == "utf-8" or chardet_text == "UTF-8":
                # print('此网页的编码格式是 UTF-8')
                return BeautifulSoup(response.text, "lxml")
            else:
                return BeautifulSoup(response.text, "lxml")


        except Exception as ex:
            self.error_reminder(ex)
            if 'latin-1' in str(ex):
                print('Headers 请求头有错误，请检查 user-agent： 或者 cookie： 等其他参数')


    def html_post(self, url, headers,data=None,ipagent=None):
        """
        html 的 bs4 解析请求网页

        :param url:请求的url地址
        :param headers:请求头部
        :param ipagent:IP代理

        :return:
        """
        """
        update log:
        1.2021年1月2日03:10:40 -- 增加了更强的编码识别


        """
        try:
            response = requests.post(url, headers=headers, data=data,timeout=10, proxies=ipagent)

            chardet_text = response.apparent_encoding

            if chardet_text == "GB2312" or chardet_text == "gb2312":
                return BeautifulSoup(response.content, 'lxml', from_encoding="gb18030")

            if chardet_text == "utf-8" or chardet_text == "UTF-8":
                return BeautifulSoup(response.content, 'lxml')

        except Exception as ex:
            self.error_reminder(ex)


    def json_get(self,url,headers,ipagent=None):
        """
        json 解析数据网页


        :param url:请求的url地址
        :param headers:请求头部
        :return:
        """
        try:
            response = requests.get(url, headers=headers, timeout=10,proxies=ipagent)
            jsondata = json.loads(response.text)
            return jsondata

        except Exception as ex:
            self.error_reminder(ex)


    def json_post(self,url,headers,data,ipagent=None):
        """
        json 解析数据网页


        :param url:请求的url地址
        :param headers:请求头部
        :return:
        """
        try:
            response = requests.post(url, headers=headers,data=data,timeout=10,proxies=ipagent)
            jsondata = json.loads(response.text)
            return jsondata

        except Exception as ex:
            self.error_reminder(ex)

class StrProcessing():
    def __init__(self):
        pass

    def split_lists(self,listinfo,number):
        """
        功能:把一个 list 分成 多个 list
        使用解释：
            list1 = [1,24,5,6,7,8,89,9,4]
            new_list = split_lists(list1,2)
            new_list 的结果就是：[[1,24],[5,6],[7,8],[89,9],[4]]

        :param listinfo: 传入的 list
        :param number: 以多少个list值，作为一个单位，形成新的 list
        :return:
        """
        list_of_group = zip(*(iter(listinfo),) * number)
        end_list = [list(i) for i in list_of_group]  # i is a tuple
        count = len(listinfo) % number
        end_list.append(listinfo[-count:]) if count != 0 else end_list
        return end_list


    def removePunctuation(self, text):
        """
        功能：获取字符串的 中文，英文，数字

        :param text:传入的字符串
        :return:
        """
        text = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",text)
        return text.strip()

    def remove_tag(self,html_document,tag_list):
        """
        去除 赛选出来的 多余不要的标签值以及标签内所有内容。

        :param html_document: 通过解析器筛选出来的HTML代码内容
        :param tag_list: html不要的标签名，需要传入一个list值
        :return:

        演示案列：

        html_content = <div>this is content <a> Unwanted content</a></div>
        上述 html_content 中去除 a 标签，
        调用函数如下：
        remove_tag(html_content,['a'])  # 此处无需赋值。
        print(html_content)

        """
        [tag.extract() for tag in html_document(tag_list)]



    def write_txt(self,contnet,filename):
        """
        写入文件

        :param contnet:写入内容
        :param filename:文件名称，可以加路径, 一定要 传入字符串 加单引号或者双引号
        :return:
        """
        with open("%s" % filename, 'a+', encoding='utf-8') as f:
            f.write(str(contnet) + '\n')
            f.close()

    def read_text(self,filename):
        """
        读取文档返回一个 list
        :param filename:文件名名称
        :return:
        """

        txt_list = []

        with open("%s" % filename, 'r', encoding='utf-8') as f:
            txt = str(f.read()).split('\n')
            for t in txt:
                if t != "":
                    txt_list.append(t)

        return txt_list

    def html_text(self,html_text_code):
        """
        获取 html 代码标签的文本内容

        :param html_code: 传入HTML 代码 【这个html代码是字符串形式】
        :return:
        """

        html = BeautifulSoup(html_text_code, 'lxml')
        content_text = str(html.find_all('html')[0].text).replace('\n','').replace(' ','').replace(' ','')
        return content_text

class SaveData():
    """
    保存文件功能

    """

    def __init__(self):
        pass


    def save_csv(self,filename,**param):
        """
        功能：保存为 csv 格式
        用法:提前要将数据先保存到自己定义的list中，然后传入值的方法为 save_csv(table_title=list,table_title=list,table_title=list,***)
            table_title : 是自己定义的保存到csv 的 表标题
            list : 是获取到的数据，添加到 list 的变量名称
            列如：
            save_csv(table_title=list,table_title=list) 表示形成一个 2列的csv 文件。
            save_csv(table_title=list,table_title=list,table_title=list) 表示形成一个3列的csv 文件。


        :param filename: 文件名称+路径，也可以不是路径
        :param param: 传入值
        :return:
        """
        csv_data = param
        csv_pd = pd.DataFrame.from_dict(csv_data, orient='index')
        tp_csv_pd = pd.DataFrame(csv_pd.values.T, index=csv_pd.columns, columns=csv_pd.index)
        tp_csv_pd.to_csv("%s.csv"%filename,encoding='gbk')


    def create_mysql(self,table_name,course_name,img_address,duration,prices,introduction,teacher,video_address):
        """
        功能：把数据保存到mysql 中
        用法解释：根据自己所需要获取的字段 。增加和修改下方 中 创建 表格的字段，和 插入数据的时候字段也要修改。以及本函数的参数也需要修改。

        创建表格字段【不在这修改】：

          course_name text,
          course_img_address text,
          course_duration text,
          course_introduction text,
          course_teacher text,
          course_video_address text

        插入表格字段【不在这修改】：
           course_name,
           course_img_address,
           ourse_duration,
           course_introduction,
           course_teacher,
           course_video_address

        传入参数修改：
        1.%(table_name,course_name,img_address,duration,introduction,teacher,video_address)
        2.create_mysql(self,table_name,course_name,img_address,duration,introduction,teacher,video_address):


        :param table_name: 数据库表名名称
        :param course_name: 课程名称
        :param img_address: 封面地址
        :param duration: 时长
        :param introduction:简介
        :param teacher: 老师名称
        :param video_address: 视频播放地址
        :return:
        """
        course_name = str(course_name).replace('\n','').replace(' ','').replace("'",'')
        introduction = str(introduction).replace('\n','').replace(' ','').replace("'",'')
        teacher = str(teacher).replace('\n','').replace(' ','').replace("'",'')
        duration = str(duration).replace('\n','').replace(' ','').replace("'",'')
        prices = str(prices).replace('\n','').replace(' ','').replace("'",'')


        con = pymysql.connect(host="localhost", user="root", password="song", database="course_db", port=3306)
        cur = con.cursor()
        # table_name = "test" # 表名称

        create_tables = """
                        create table if not exists %s(
                        id int(10) auto_increment primary key,
                        course_name mediumtext,
                        course_img_address mediumtext,
                        course_duration mediumtext,
                        course_prices mediumtext,
                        course_introduction mediumtext,
                        course_teacher mediumtext,
                        course_video_address mediumtext
                        )

                    """ % ("%s"%table_name)

        cur.execute(create_tables)
        con.commit()

        #插入数据
        # course_name = "test" #课程名称
        # img_address = "test" #课程封面地址
        # duration = "test" #课程时长
        # introduction = "test" # 简介
        # teacher = "test" # 老师
        # video_address = "test" # 视频地址
        print(course_name, f"--------------------------------------写入了{table_name}数据库中")
        sql_insert_data ="""
                insert into %s(
                        course_name,
                        course_img_address,
                        course_duration,
                        course_prices,
                        course_introduction,
                        course_teacher,
                        course_video_address
                ) value (

                        '%s',
                        '%s',
                        '%s',
                        '%s',
                        '%s',
                        '%s',
                        '%s'
                );

        """ %(table_name,course_name,img_address,duration,prices,introduction,teacher,video_address)

        cur.execute(sql_insert_data)
        con.commit()

    def other_create_mysql(self,table_name,title,content,release_time):


        #
        # title = str(title).replace('\n','').replace(' ','').replace("'",'')
        # content = str(content).replace('\n','').replace(' ','').replace("'",'')
        # release_time = str(release_time).replace('\n','').replace(' ','').replace("'",'')
        #

        con = pymysql.connect(host="localhost", user="root", password="song", database="other", port=3306)
        cur = con.cursor()


        create_tables = """
                        create table if not exists %s(
                        id int(10) auto_increment primary key,
                        title text,
                        content mediumtext,
                        release_time text

                        )

                    """ % ("%s"%table_name)

        cur.execute(create_tables)
        con.commit()

        print(title, f"--------------------------------------写入了{table_name}数据库中")

        sql_insert_data ="""
                insert into %s(
                        title,
                        content,
                        release_time

                ) value (

                        '%s',
                        '%s',
                        '%s'
                     
                );

        """ %(table_name,title,content,release_time)

        cur.execute(sql_insert_data)
        con.commit()



if __name__ == '__main__':
    toos = SaveData().other_create_mysql("a",title='123',content='asd',release_time='d123132')

