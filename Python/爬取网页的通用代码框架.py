# -*- coding: utf-8 -*-
"""
Created on Mon May 29 20:54:58 2017

@author: xiaoxiao
"""
import requests

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()#如果状态不是200,引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"
if __name__=="__main__":
    url="http://www.baidu.com"
    print(getHTMLText(url))
