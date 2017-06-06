# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 10:00:16 2017

@author: xiaoxiao
"""

import requests

#url="http://m.ip138.com/ip.asp?ip="
#r=requests.get(url+'202.204.80.112')#202.204.80.112是北理首页的IP地址
#print(r.status_code)
#
##查看返回文本的相关内容
#print(r.text[-500:])#返回文本的最后500字节

url="http://m.ip138.com/ip.asp?ip="
try:
    r=requests.get(url+'202.204.80.112')
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")      
      