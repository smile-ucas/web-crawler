# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 10:57:38 2017

@author: xiaoxiao
"""
#http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html
#http://www.zuihaodaxue.com/robots.txt   结果404not find，所以这个网站没有robots协议
#步骤1：从网络上获取网页内容 getHTMLText()
#步骤2：提取网页内容中信息到合适的数据结构(这里可以用二维列表，列表中的每个元素又是一个列表) fillUnivList()
#步骤3：利用数据结构展示并输出结果 printUnivList()

    
import requests
from bs4 import BeautifulSoup   #这里引用的是bs4库的BeautifulSoup类
import bs4 #这里引用的是bs4库
 
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()#产生异常信息
        r.encoding = r.apparent_encoding#修改编码
        return r.text
    except:
        return ""
 
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")#观察要爬取数据的格式特点  每一个大学的信息都在一个tr中,所有的tr在tbody中
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')#将所有的td标签存到一个列表类型中tds
            ulist.append([tds[0].string, tds[1].string, tds[3].string])
 
def printUnivList(ulist, num): #第二个参数num指需要将多少个学校（元素）打印,需要格式化输出
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校名称","总分"))
    for i in range(num):
        u=ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
     
def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20) # 20 univs
main()    



