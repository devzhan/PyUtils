# -*- coding: UTF-8 -*-
# BeautifualSoup学习 http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id30
from bs4 import BeautifulSoup as BS
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister oo" id="link1" >Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup=BS(html_doc,"html.parser")
# 获取a标签，返回类型Tag
tagA=soup.a
# tag的名称
print(tagA.name)
print(tagA.attrs)
# tagA.name='aa'
# print(tagA.name)
print(tagA.string+'a')
# 获取tag不同属性的值
print(tagA['id'])
print(tagA.get('class'))
# 遍历所有的a 标签 返回的是一个tag的list
for link in soup.find_all('a'):
    print(link.get('href'))
    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie

last_a_tag = soup.find("a", id="link3")
print(last_a_tag.string)
import re
for tag in soup.find_all(re.compile("t")):
    print(tag.name)
link2=soup.find_all(href="http://example.com/tillie")
print(link2)

links=soup.find_all(class_="sister")
print(links)
print(soup.find_all(string=re.compile("l")))