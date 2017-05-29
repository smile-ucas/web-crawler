# -*- coding: utf-8 -*-
"""
Created on Mon May 29 16:42:27 2017

@author: xiaoxiao
"""

import requests

r=requests.get("http://www.baidu.com")
print(r.status_code)
r.encoding='utf-8'
print(r.text)

