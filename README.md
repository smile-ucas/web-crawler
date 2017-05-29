# Python爬虫
## [Requests库](http://www.python-requests.org)

**以管理员身份打开命令提示符，运行pip install requests,即可安装Requests**

**Requests库的7个主要方法** 

***requests.request()***

构造一个请求，是以下各方法的基础方法; 返回Response对象，命为r;r.status_code若为200，则返回成功；r.text是url对应的页面内容；r.encoding是从http header中猜测出来的响应内容的编码方式；r.apparent_encoding是从内容中分析出来的响应内容的编码方式（备选编码方式）;r.content是http响应内容的形式

http是一个基于“请求与响应”模式的、无状态的应用层协议。（无状态指的是前一次请求和后一次请求没有关系）

***requests.get()***

获取html网页的主要方法，对应于http的get

***requests.head()***

获取html网页头信息的主要方法，对应于http的head

***requests.post()***

向html网页提交post请求的方法，对应于http的post

***request.put()***

向html网页提交put请求的方法，对应于http的put

***request.patch()***

向html网页提交布局修改请求，对应于http的patch

***request.delete()***

向html网页提交删除请求，对应于http的delete


