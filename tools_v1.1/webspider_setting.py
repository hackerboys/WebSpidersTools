#encoding:utf-8
import spider_tools
import time
import os
import ast
from fake_useragent import UserAgent


get_tools = spider_tools.Getweb_tools() # 请求网页快捷工具
str_tools = spider_tools.StrProcessing() # 处理字符串，获取HTML代码文字内容，写入，读取文本等工具
save_tools = spider_tools.SaveData() # 保存数据工具 - 目前可保存为 mysql 以及 csv


#随机请求头的User-agent,取消注释表示开启。

# user_agent = UserAgent().random

"""
用法演示：
用之前请 安装 fake-useragent 安装注意并非下滑线，调用时要 - 改成 _ 下滑线。
pychram 请在 设置安装或在pycharm 打开终端 输入 pip install fake-useragent 

headers= {

    "cookie":"",
    "user-agent":user_agent
        ...
}

response = requests.get(url,headers=headers)
print(response.text)

"""



# 代理的设置，请重新按照代理网接入文档写。如何调用下方以参考


"""

下方为代理案列，代理网站是 小象代理案列，使用时请按照实际购买的IP代理的接入文档写
*******************************************************
target_url = "http://api.ip.sb/ip"
proxy_host = 'http-dynamic.xiaoxiangdaili.com'
proxy_port = 10030
proxy_username = '应用id（后台-产品管理-隧道代理页面可查）'
proxy_pwd = '应用密码（后台-产品管理-隧道代理页面可查）'

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxy_host,
    "port": proxy_port,
    "user": proxy_username,
    "pass": proxy_pwd,
}

proxies = {
    'http': proxyMeta,
    'https': proxyMeta,
}
*******************************************************


只要调用：proxies 值即可：
代码调用代理实例：

def index():

    html = get_tools.html_get(url,headers=headers,ipagent=proxies)
    print(html)
    

推荐代理：快代理：https://www.kuaidaili.com/ 【隧道动态IP代理】
推荐代理：小象代理：https://www.xiaoxiangdaili.com/tunnel-short 【隧道动态IP代理】，没有快代理的稳定。但是便宜。

"""



