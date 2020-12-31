#encoding:utf-8
from bs4 import BeautifulSoup
import json
import requests
import threading
import pymysql
import pandas as pd
import ast
from tool_magazine import *
tools = Toolmagezine()


#数据保存位置
data_save_path = r"D:\PythonPro\DataCollection36\WebSpiders\save_data"



# 付费代理IP设置。

# def ip_agent():
#     """
#     付费代理IP，API设置。
#
#     :return:
#     """
#     ipapi = "" # 付费代理API
#     respon = requests.get(ipapi)
#
#     ip_port = json.loads(respon.content)['data']['proxy_list'][0]  # 根据代理网站，自行修改此处代码
#     print(ip_port)
#     return ip_port



# 函数式多线程 演示：

# glock = threading.Lock() #多线程锁
# url_list = [] # 讲要请求的 url,保存到list 中
#
#
# def runs():
#     while True:
#         glock.acquire()
#         if len(url_list) == 0:
#             glock.release()
#             break
#         glock.release()
#         url = url_list.pop()
#
#
#         headers = {
#             'user_agent':'',
#             'cookie':''
#
#         }
#
#
#         response = requests.get(url,headers = headers)
#         print(response.text)
#
# for x in range(5): # 开启5个线程执行程序
#
#     r = threading.Thread(target=runs) # runs 是上方函数名，不能加括号。
#     r.start()



