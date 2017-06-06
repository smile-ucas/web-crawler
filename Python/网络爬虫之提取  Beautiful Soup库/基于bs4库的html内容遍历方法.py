# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
       


r=requests.get("http://python123.io/ws/demo.html")
demo =r.text

soup = BeautifulSoup(demo,"html.parser")

#print(soup.head)#<head><title>This is a python demo page</title></head>
#print(soup.head.contents) #[<title>This is a python demo page</title>]
#
#print(len(soup.body.contents))#5 长度
   
#print(soup.body.contents[1])#<p class="title"><b>The demo python introduces several python courses.</b></p>

#遍历儿子节点
#for child in soup.body.children:
#    print(child)

##遍历子孙节点     
#for child in soup.body.children:
#    print(child)
     
#遍历（标签树的上行遍历）
#.parent  节点的父亲节点
#.parents  节点先辈标签的迭代类型，用于循环遍历先辈节点     
#print(soup.title.parent)  #title的父亲节点   <head><title>This is a python demo page</title></head>
#print(soup.html.parent)  #html的父亲就是它自己
#print(soup.parent)#None

soup = BeautifulSoup(demo,"html.parser")
#for parent in soup.a.parents:   #找a标签的父亲
#    if parent is None:
#        print(parent)
#    else:
#        print(parent.name)
#        #结果：p
#        #     body
#        #     html
#        #     [document]


##遍历（标签树的平行遍历，必须发生在同一个父亲节点下的各节点间）
#print(soup.a.next_sibling) #and 所以不能认为平行遍历得到的一定是标签类型

     
#print(soup.a.next_sibling.next_sibling) #<a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>
#
#for sibling in soup.a.next_siblings:
#    print(sibling)
#     
#for sibling in soup.a.previous_siblings:
#    print(sibling)

















