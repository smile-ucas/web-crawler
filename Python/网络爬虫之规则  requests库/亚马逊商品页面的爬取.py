# -*- coding: utf-8 -*-
#"""
#Created on Tue May 30 20:43:06 2017
#
#@author: xiaoxiao
#"""

import requests

#r =requests.get("https://www.amazon.cn/gp/product/B01M8L5Z3Y")
#print(r.status_code)#200
#
##如果r.status_code不是200，那么需要把r.encoding=r.apparent_encoding
#
#print(r.request.headers)
##{'User-Agent': 'python-requests/2.12.4', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}


url="https://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
    kv={'user-agent':'Mozilla/5.0'}
    r=requests.get(url,headers=kv)
    #当发生错误时，可以修改headers内容
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")
