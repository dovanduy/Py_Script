# coding:utf-8
from lxml import etree
import re
import requests
import string
from requests.sessions import Session

# 新浪新闻
# response = Session().request('get', 'https://mil.news.sina.com.cn/')
# response = requests.get('https://mil.news.sina.com.cn/')
response = requests.request('GET', 'https://mil.news.sina.com.cn/')
response.close()
# print response.text
html = etree.HTML(response.text)

# 最新新闻
result = html.xpath('//div[@class="zgjq"]//ul//a')
print len(result)
for li in result:
    titlt = li.xpath('./text()')
    if len(titlt):
        print titlt[0],
        print li.xpath('./@href')
# newurl = result[0].xpath('.//a/@href')[0]
# print newurl
# response = requests.get(newurl)
