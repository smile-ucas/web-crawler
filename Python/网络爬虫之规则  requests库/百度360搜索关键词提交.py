# -*- coding: utf-8 -*-
"""
Created on Tue May 30 22:12:56 2017

@author: xiaoxiao
"""

import requests

#提交关键词 获得搜索结果
#搜索引擎关键词提交接口 http://www.baidu.com/s?wd=keyword     http://www.so.com/s?q=keyword
#kv={'wd':'Python'}
#r= requests.get("http://www.baidu.com/s",params=kv)
#print(r.status_code)
#print(r.request.url)   #http://www.baidu.com/s?wd=Python
#print(len(r.text))  #312419(长度)

keyword="Python"
try:
    key={'q':keyword}
    r = requests.get("http://www.so.com/s",params=kv)
    print(r.request.url)  
    r.raise_for_status()
    print(len(r.text)) 
    print(r.text) 
except:
    print("爬取失败") 