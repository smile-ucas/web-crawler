# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 16:54:30 2017

@author: xiaoxiao
"""

import requests
from bs4 import BeautifulSoup
import traceback
import re



#1.从东方财富网获取股票列表(http://quote.eastmoney.com/stocklist.html)
#2.根据股票列表逐个到百度股票获取个股信息（https://gupiao.baidu.com/stock）
#把结果存储到文件

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
 
def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser') 
    a = soup.find_all('a')  #观察东方财富网的源码，可以发现股票码都在a标签中
           #<li><a target="_blank" href="http://quote.eastmoney.com/sh203018.html">0504R091(203018)</a></li>
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])#sh203018  在上面的a标签中找到的就是sh203018，以s开头，之后是h或z，然后跟着6个数字
        except:
            continue
 
def getStockInfo(lst, stockURL, fpath):
    ############################################################
    count=0 #这里这个变量是为了显示爬取过程中的进度条，提高用户体验
    ############################################################
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html=="":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div',attrs={'class':'stock-bets'}) #找到这个div标签
 
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]  #例如  <a class="bets-name" href="/stock/sh000001.html">
            infoDict.update({'股票名称': name.text.split()[0]}) #将信息增加到字典中 这里用split是以防有的信息中去掉后面多余的
             
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text  
                val = valueList[i].text
                infoDict[key] = val
                        
             #保存在文件
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write( str(infoDict) + '\n' )
                ############################################################
                count=count+1
                
                print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
                ############################################################
        except:
            ############################################################
            count=count+1
                
            print("\r当前进度: {:.2f}%".format(count*100/len(lst)),end="")
            ############################################################
            traceback.print_exc()
            continue
 
def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'D:/BaiduStockInfo.txt'
    slist=[]
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)
 
main()








