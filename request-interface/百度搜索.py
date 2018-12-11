# coding:utf-8
import requests

uri = 'https://www.baidu.com/s'
params = {'ie': 'UTF-8', 'wd': 'cz9025'}
headers = {'Content-Type': 'text/html'}
# params = {'wd':'python'}

response = requests.get(uri, params=params, headers=headers)
print response.url
print response.status_code
# print params
print response.text
