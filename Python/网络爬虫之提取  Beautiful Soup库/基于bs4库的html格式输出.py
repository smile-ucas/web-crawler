# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 10:47:10 2017

@author: xiaoxiao
"""


import requests
from bs4 import BeautifulSoup

r=requests.get("http://python123.io/ws/demo.html")
demo =r.text
soup = BeautifulSoup(demo,"html.parser")


#格式非常清晰
#print(soup.prettify())
print(soup.a.prettify())

