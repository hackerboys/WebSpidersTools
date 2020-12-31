#encoding:utf-8
from web_setting import *


class Toolmagezine():
    """
    爬取网页的所用到的常用工具集合

    """
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

    def html_requests(self,url, headers):
        """
        html 的 bs4 解析请求网页

        :param url:请求的url地址
        :param headers:请求头部
        :return:
        """
        self.url = url
        self.headers = headers


        response = requests.get(self.url, headers=self.headers, timeout=10)
        html = BeautifulSoup(response.content, 'lxml')
        return html

    def json_requests(self,url,headers):
        """
        json 解析数据网页


        :param url:请求的url地址
        :param headers:请求头部
        :return:
        """
        response = requests.get(url, headers=headers, timeout=10)
        jsondata = json.loads(response.text)
        return jsondata

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
        con = pymysql.connect(host="localhost", user="root", password="song", database="course_db", port=3306)
        cur = con.cursor()
        # table_name = "test" # 表名称

        create_tables = """
                        create table if not exists %s(
                        id int(10) auto_increment primary key,
                        course_name text,
                        course_img_address text,
                        course_duration text,
                        course_prices text,
                        course_introduction text,
                        course_teacher text,
                        course_video_address text
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








