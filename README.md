# Python爬虫
## [Requests库](http://www.python-requests.org)  爬取网页，小规模，数据量小，爬取速度不敏感

**以管理员身份打开命令提示符，运行pip install requests,即可安装Requests**

**Requests库的7个主要方法** 

***requests.request()*** 

构造一个请求，是以下各方法的基础方法; 返回Response对象，命为r;r.status_code若为200，则返回成功；r.text是url对应的页面内容；r.encoding是从http header中猜测出来的响应内容的编码方式；r.apparent_encoding是从内容中分析出来的响应内容的编码方式（备选编码方式）;r.content是http响应内容的形式

http是一个基于“请求与响应”模式的、无状态的应用层协议。（无状态指的是前一次请求和后一次请求没有关系）

requests.request(method,url,**kwargs)

其中，method有7种:GET、HEAD、POST、PUT、PATCH、delete、OPTIONS,用单引号括起来

第三个参数控制访问的参数（共13个），均为可选项；其中，params是字典或字节序列，作为参数增加到url中（params=zidian）；data是字典、字节序列或文件对象，作为Request的内容（data=zidian  data=zifuchuan）;json,JSON格式的数据，作为Request的内容（json=zidian）；headers,字典，http定制头（headers={'user-agent':'Chrome/10'}）;cookies,字典或CookieJar，Request中的cookie;auth，元组，支持http认证功能；files，字典类型，向服务器传输文件时使用的字段，从而可以向某一个url链接提交某一个文件；timeout，设置超时时间，单位秒；proxies，字典类型，设定访问代理服务器，可增加登录认证；allow_redirects，允不允许对url进行重定向，重定向开关，默认为True；stream，也是开关，对获取内容是否立即下载，默认为True；verify，也是开关，认证SSL证书的开关，默认为True；cert，保存本地SSL证书路径的字段；

***requests.get()*** ***常用***

获取html网页的主要方法，对应于http的get

requests.get(url,params=None,**kwargs)  

其中，第二个参数（可选）就是requests.request()中第三个可选参数中的params参数，第三个参数（可选）有12个，就是requests.request()中第三个参数中除了params的其余的12个参数

***requests.head()***

获取html网页头信息的主要方法，对应于http的head

requests.head(url,**kwargs)

第二个参数（可选）有13个，与requests.request()中第三个参数完全一样

***requests.post()***

向html网页提交post请求的方法，对应于http的post（请求向URL位置的资源后附加新的数据）；当向URL post一个字典或键值对时，会自动编码为form（表单）；向URL post一个字符串，会自动编码为data下；(put方法也类似，只不过它能将原有的数据覆盖掉，put请求向URL位置存储一个资源，覆盖原来URL位置的资源)

...

"data":"..."

"form":{},

...

requests.post(url,data=None,json=None,**kwargs)

其中，第2、3个参数和requests.request()中第三个参数的data和json参数是一样的，第四个参数（可选）11种，就是requests.request()中第三个参数中剩下的11种

***request.put()***

向html网页提交put请求的方法，对应于http的put；比如有20个字段，要求改其中一个字段，put需要把另外不需要改的19个字段都得写上，否则会被删除

requests.put(url,data=None,**kwargs)

其中，第2个参数和requests.request()中第三个参数的data参数是一样的，第3个参数（可选）12种，就是requests.request()中第三个参数中剩下的12种

***request.patch()***

向html网页提交布局修改请求，对应于http的patch；比如有20个字段，要求改其中一个字段，patch只需要写那个需要被改的字段就行，patch能节省网络带宽

requests.patch(url,data=None,**kwargs)

其中，第2个参数和requests.request()中第三个参数的data参数是一样的，第3个参数（可选）12种，就是requests.request()中第三个参数中剩下的12种

***request.delete()***

向html网页提交删除请求，对应于http的delete（请求删除URL位置存储的资源）

requests.delete(url,**kwargs)

第2个参数可选13种，就是requests.request()中第三个参数中的13种

## Scrapy库 中规模，数据规模较大，爬取速度敏感，爬取网站，爬取系列网站;



## 大规模，搜索引擎，爬取速度关键，爬取全网，没有第三方库，要定制开发


## 对爬虫的限制

**Robots协议(发布公告，哪些不可以爬)，如果没有这个协议，表示这个网站允许所有爬虫无限制爬**

Robots协议的基本语法：User-Agent：*（这个代表所有爬虫）      Disallow:/  (/代表根目录)
 
http://www.baidu.com/robots.txt

**来源审查（判断User-Agent进行限制）维护网站的技术人员来设定的**

检查http协议头的User-Agent域，只响应浏览器或友好爬虫的访问


