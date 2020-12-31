#encoding:utf-8
"""
功能：生成 headers 的字典数据，不用一个一个 去添加 逗号
用法：
在 浏览器 F12 的 network 中 复制到 请求头（headers） cookie ,user-agent,referer,host 等一些信息，粘贴到 cookietest 中，运行本程序即可,得到结果复制到爬虫程序的 headers 中

"""

# 在下方添加，复制过来的请求头信息。

cookietext = """

Cookie: PHPSESSID=tssped46bj57n1g08m2bd2acm4; Hm_lvt_4dd9333727c5761fa697d2fd1bf6ab1a=1609332337,1609350925; online-uuid=3117D12D-F8CF-32E8-B000-66DE030A470F; Hm_lpvt_4dd9333727c5761fa697d2fd1bf6ab1a=1609402954
Host: www.taikr.com
sec-ch-ua: "Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"
sec-ch-ua-mobile: ?0
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36

"""


cook_list = cookietext.split('\n')
for cl in cook_list:
    if cl != "":
        newcl = cl.split(': ')
        cookename = newcl[0]
        cookevalue = newcl[1]
        cookiestr = "'%s':'%s'," %(cookename,cookevalue)
        print(cookiestr)


#结果演示：

# headers  = {
#
# 'Cookie':'_lxsdk_cuid=176afffd70ac8-0ad2f5a403bd91-c791039-384000-176afffd70ac8; _lxsdk=176afffd70ac8-0ad2f5a403bd91-c791039-384000-176afffd70ac8; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1609270549; _hc.v=2b18af6d-811d-6bf5-3c47-a7402d8a5524.1609270549; lgtoken=0859b6263-bc04-497f-ac2e-8075d64d3d6a; dplet=66afb76911e965b39e6fd884a7cb8c87; dper=09cb028b57aa5feecee98e3f86c1766d6f48d95bbc640d48d9bd285bbbb7ca71e044c6aadf0112b5d46ea4217f940e036fe59040521f38bc0f12ee10993d61d6b590c4ec95e6cabd260b9556bedfbdc311880bbf08edce72683721c95cd142af; ll=7fd06e815b796be3df069dec7836c3df; ua=%E5%8C%97%E7%83%9F_1106; ctu=0e0b2b9cae69a5158e0494e23c1da20f0e3b46fbfb6c8b772ee8fd53deb0a861; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1609270584; _lxsdk_s=176afffc975-2bc-227-50c%7C693144158%7C253',
# 'Host':'www.dianping.com',
# 'Upgrade-Insecure-Requests':'1',
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
#
#
# }




