# coding:utf-8
import re
from lxml import etree
import requests
import time

# https://www.thepaper.cn/load_index.jsp?&pageidx=2&lastTime=1542792862258

list_time = str(time.time()).split('.')
if int(list_time[1]) < 100:
    list_time[1] = '100'
last_time = list_time[0] + list_time[1]
print last_time, type(last_time)
uri = 'https://www.thepaper.cn/'
params = 'load_index.jsp?&pageidx=2&lastTime=' + last_time
url = uri + params
print url
response = requests.get(url)
print 'headers=>>>', response.headers
print response.status_code  # 响应的状态码
# print response.content   # 返回字节信息
# print response.text  # 返回文本内容

html = etree.HTML(response.text)

a_tesult = html.xpath('//h2/a')
for a in a_tesult:
    a_img = a.xpath('./../../div[1]/a/img/@src')

    atext = a.xpath('./text()')
    ahref = a.xpath('./@href')
    print atext[0], uri + ahref[0],a_img

