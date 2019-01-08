# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 17:30
# @Author  : cz9025
# @File    : 今日头条.py
# @Software: PyCharm

from pyquery import PyQuery
from lxml import etree
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
response = requests.get(url="https://www.toutiao.com/ch/investment/", headers=headers)
print response.status_code
print response.content
html = etree.HTML(response.text)
ul = html.xpath("ul[contains(@class,'slide-list')]")
# print ul


pq = PyQuery("https://www.toutiao.com", headers)
# print pq
