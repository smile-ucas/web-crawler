# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 10:14:23 2017

@author: xiaoxiao
"""

#https://www.crummy.com/software/BeautifulSoup/
#安装 以管理员权限启动cmd，输入pip install beautifulsoup4
#安装的小测 演示HTML页面地址http://python123.io/ws/demo.html

import requests
from bs4 import BeautifulSoup
r=requests.get("http://python123.io/ws/demo.html")
#print(r.text)
demo =r.text



soup=BeautifulSoup(demo,"html.parser")#使用html的解析    把标签树变成BeautifulSoup类
print(soup.prettify())
print(soup.title) #<title>This is a python demo page</title>

print(soup.a) #如果有多个a标签，则只显示第一个a标签  <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>
print(soup.a.name)#a
print(soup.a.parent.name)#p
print(soup.p.parent.name)#body

     
tag=soup.a
print(tag.attrs)#{'href': 'http://www.icourse163.org/course/BIT-268001', 'class': ['py1'], 'id': 'link1'}
print(tag.attrs['href'])#http://www.icourse163.org/course/BIT-268001
print(type(tag.attrs))#<class 'dict'>
print(type(tag))#<class 'bs4.element.Tag'>

print(tag.string)#     Basic Python  ,这个显示这个标签上两个<><>之间的内容
print(type(tag.string))#     <class 'bs4.element.NavigableString'>
     
     
     
     
     
     