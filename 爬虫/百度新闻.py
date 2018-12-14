# coding:utf-8
from lxml import etree
import re
import requests
from pyquery import PyQuery

# https://www.thepaper.cn/channel_masonry.jsp?channelID=25950
# https://www.thepaper.cn/load_index.jsp?&pageidx=2&lastTime=1542790579509
# 百度新闻
response = requests.get('https://news.baidu.com/guonei')
print response.text
html = etree.HTML(response.text)

# 最新新闻
result = html.xpath('//ul[contains(@class,"ulist")]//a')
print len(result)
for li in result:
    print li.xpath('./text()'),
    print li.xpath('./@href')
# newurl = result[0].xpath('.//a/@href')[0]
# print newurl
# response = requests.get(newurl)


# 这个只适合解析html
pq = PyQuery(response.content)

result = pq('a').eq(0).attr('href')

print result
