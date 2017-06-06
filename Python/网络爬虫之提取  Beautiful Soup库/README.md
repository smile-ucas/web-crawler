# [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
# 安装 

**以管理员权限启动cmd，输入pip install beautifulsoup4**

# 安装的小测

**演示HTML页面地址http://python123.io/ws/demo.html**

## 标签 soup.a

## 名称 .name //得到例如标签"a"

## 属性 .attrs  //得到某属性

## 非属性字符串/注释 .string  //得到<><>之间的内容

#遍历（遍历儿子和子孙）

**使用for in**

#遍历（标签树的上行遍历）

.parent  节点的父亲节点

.parents  节点先辈标签的迭代类型，用于循环遍历先辈节点


#遍历（标签树的平行遍历，必须发生在同一个父亲节点下的各节点间）不能认为平行遍历得到的一定是标签类型

**.next_sibling**

**.previous_sibling**

**.next_siblings**   返回所有后续的平行节点标签

**.previous_siblings**
 

``` python

for sibling in soup.a.next_siblings:

    print(sibling)

     
for sibling in soup.a.previous_siblings:

    print(sibling)


``` 





