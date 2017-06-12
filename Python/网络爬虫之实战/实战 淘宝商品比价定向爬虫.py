# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 16:54:30 2017

@author: xiaoxiao
"""

import re
import requests
#此例子仅仅用来学习技术，并不会不加限制的爬取

#淘宝搜索“防晒衣”
#第一页https://s.taobao.com/search?q=%E9%98%B2%E6%99%92%E8%A1%A3&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20170608&ie=utf8&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s=0
#第二页https://s.taobao.com/search?q=%E9%98%B2%E6%99%92%E8%A1%A3&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20170608&ie=utf8&bcoffset=1&ntoffset=1&p4ppushleft=1%2C48&s=44
#第三页https://s.taobao.com/search?q=%E9%98%B2%E6%99%92%E8%A1%A3&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20170608&ie=utf8&bcoffset=1&ntoffset=1&p4ppushleft=1%2C48&s=88
#不同之处是尾处s=0 44 88 因为每页商品44件


#采用正则  获取商品名称和价格
def geHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()#产生异常信息
        r.encoding = r.apparent_encoding#修改编码
        return r.text
    except:
        return ""

def parsePage(ilt,html):
    try:
#        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)   #可以看网页源代码，比如价格的代码是"view_price":"99.80"
#        tlt=re.findall(r'\"raw_title\"\:\"'*?\"',html)  #其中*?最小匹配，商品名称代码"raw_title":"夏装宽松中长款风衣韩版薄款白色外套休闲收腰显瘦防晒衣短外套女"
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])#去掉前面的view_price字段 只获得数字价格部分 eval函数能将获得的字符串的最外层的单引号双引号去掉
            title = eval(tlt[i].split(':')[1])
            ilt.append([price , title])
    except:
        print("")
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
         
    
def main():
    goods='防晒衣'
    depth=2
    start_url='https://s.taobao.com/search?q='+goods
    infoList=[]
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
     
main()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        