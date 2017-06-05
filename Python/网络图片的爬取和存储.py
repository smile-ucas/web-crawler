# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 19:08:37 2017

@author: xiaoxiao
"""

import requests
path ="E:/abc.jpg"
url="http://exp.cdn-hotels.com/hotels/4000000/3900000/3893200/3893187/3893187_25_y.jpg"
r=requests.get(url)
print(r.status_code)
with open (path,'wb')as f:#打开文件
    f.write(r.content)   #r.content得到二进制格式
f.close()


