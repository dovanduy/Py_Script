# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 17:30
# @Author  : cz9025
# @File    : 环球.py
# @Software: PyCharm
import requests
from pyquery import PyQuery

pq = PyQuery("http://world.huanqiu.com", encoding='utf-8')
div = pq("#foucsBox ul.imgCon")
# print div.html()
li = div.find("li")
# print li.html()
for i in li.items():
    # print i.filter("li a").html()
    img = i.find("a").eq(0).find("img").attr("src")
    a = i.find(".imgTitle>a")
    href = a.attr("href")
    txt = a.html()
    if img:
        print txt, href
        print img


response = requests.get(url="http://world.huanqiu.com")
print response.encoding