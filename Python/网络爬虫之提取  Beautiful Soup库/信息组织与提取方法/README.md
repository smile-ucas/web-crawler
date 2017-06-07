# 信息标记3种形式（世界上所有的信息都可以通过这3种表示）

XML

JSON（类型键值对）

YAML (无类型键值对，不加""，用缩进，|表示整块数据，#注释)

# <>.find_all(name,attrs,recursive,string,**kwargs)

**返回一个列表类型，存储查找的结果**

例如，soup.find_all('a')//a标签

soup.find_all(['a','b'])//a、b标签

```
for tag in soup.find_all(True)

	print(tag.name) //所有标签的名字被打印
```

**想要打印以“b”开头的标签（例如b标签，body标签，要先引入郑州表达式库，import re** 

```
for tag in soup.find_all(re.compile('b'))

	print(tag.name) 
```

**第二个参数attrs,表示带有该属性的...**


soup.find_all('p','course') // 返回带有course属性的p标签

soup.find_all(id='link1') //返回id为link1的标签，若没有，则返回[]

soup.find_all(id=re.compile('link')) //返回id以link开头的标签

**第三个参数recursive,是否对子孙全部检索，默认为True**

soup.find_all('a',recursive=False) //检索儿子节点


**参数string  <>...</>中字符串区域的检索字符串**

soup.find_all(string='Basic Python ...一些内容')  //若有，则返回['Basic Python ...一些内容']

soup.find_all(string=re.compile('python')) //返回含有python的字符串


#  < tag> (..)  等价于 <tag>.find_all(..)

#  < soup>(..)  等价于 <soup>.find_all(..)



# <>.find()  //返回一个结果，字符串类型，和.find_all()参数一样

# <>.find_parents()  //返回列表类型，和.find_all()参数一样

# <>.find_parents()  //返回一个结果，字符串类型，和.find_all()参数一样

# <>.find_next_sibling()  //返回一个结果，字符串类型，和.find_all()参数一样

# <>.find_next_siblings()  //返回列表类型，和.find_all()参数一样

# <>.find_previous_sibling()  //返回一个结果，字符串类型，和.find_all()参数一样

# <>.find_previous_siblings()  //返回列表类型，和.find_all()参数一样