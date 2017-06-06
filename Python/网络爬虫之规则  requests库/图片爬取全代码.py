# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 21:57:15 2017

@author: xiaoxiao
"""

import requests
import os
root ="E://"
url="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1496638785417&di=ece9447a834357c99cbc598219db60ea&imgtype=0&src=http%3A%2F%2Fwww.taisha.org%2Fuploadfile%2F2017%2F0518%2F20170518105125776.jpg"
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

