# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 21:57:15 2017

@author: xiaoxiao
"""

import requests
import os
root ="E:/example.jpg"
url="http://exp.cdn-hotels.com/hotels/4000000/3900000/3893200/3893187/3893187_25_y.jpg"
path=root+url.split('/')[-1]
try:
    if not os.path.exist(root):
        os.makir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb')as f:
            f.write(r.content)
            f.close()   
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")

