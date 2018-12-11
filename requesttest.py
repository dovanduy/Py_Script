# coding:utf-8

import requests
import json

# url = "http://www.baidu.com/s"
# params = {'ie': 'UTF-8', 'wd': 'cz9025'}
# 可以加头，缓存，参数，超时timeout
# # r=requests.get(url,params)
# r = requests.get("https://github.com/timeline.json")

url = 'http://httpbin.org/post'
# post请求添加文件操作
files = {'file': open('a.txt', 'rb')}
r = requests.post(url, files=files)
# r是属于response对象
print r
# 允许重定向
# r=requests.get(url,allow_redirects=True)
print r.url
print r.text
print requests.codes.ok
print r.headers
print r.history
print r.status_code
print r.reason
s = requests.session()
requests.Request
requests.Session
requests.session()
print s
