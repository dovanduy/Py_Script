# coding:utf-8
from lxml import etree
import re
import requests
from pyquery import PyQuery

# https://www.thepaper.cn/channel_masonry.jsp?channelID=25950
# https://www.thepaper.cn/load_index.jsp?&pageidx=2&lastTime=1542790579509
# 百度新闻
response = requests.get('https://news.baidu.com')

pq=PyQuery(response.text)
top= pq("#pane-news>div>ul").find("li")
bot= pq("#pane-news>ul:first").find("li")
strs=top+bot
for i in strs.items():
    print i.find("a").html(),i.find("a").attr("href")

