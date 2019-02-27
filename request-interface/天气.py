# coding:utf-8
import requests

uri = 'http://t.weather.sojson.com/api/weather/city/101030100'
# params = {'ie': 'UTF-8', 'wd': 'cz9025'}
headers = {'Content-Type': 'text/html'}

response = requests.get(url=uri,headers=headers)
print response.url
print response.status_code
print response.content
print response.json()
