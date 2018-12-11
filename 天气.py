# -*- coding: utf-8 -*-
# import urllib2
#
# url1 = 'http://m.weather.com.cn/data5/city.xml'
# content1 = urllib2.urlopen(url1).read()
# provinces = content1.split(',')
# result = 'city = {\n'
# url = 'http://m.weather.com.cn/data3/city%s.xml'
# for p in provinces:
#     p_code = p.split('|')[0]
#     url2 = url % p_code
#     content2 = urllib2.urlopen(url2).read()
#     cities = content2.split(',')
#     for c in cities:
#         c_code = c.split('|')[0]
#         url3 = url % c_code
#         content3 = urllib2.urlopen(url3).read()
#         districts = content3.split(',')
#     for d in districts:
#         d_pair = d.split('|')
# d_code = d_pair[0]
# name = d_pair[1]
# url4 = url % d_code
# content4 = urllib2.urlopen(url4).read()
# code = content4.split('|')[1]
# line = " '%s': '%s',\n" % (name, code)
# result += line
# print name + ':' + code
# result += '}'
# f = file('/home/crossin/Desktop/city.py', 'w')
# f.write(result)
# f.close()



import urllib2
import json
from city import city

cityname = raw_input("you like who ciyt")
citycode = city.get(cityname)
if citycode:
	try:
		url = ('http://www.weather.com.cn/data/cityinfo/%s.html'% citycode)
		content = urllib2.urlopen(url).read()
		data = json.loads(content)
		result = data['weatherinfo']
		str_temp = ('%s\n%s ~ %s') % (result['weather'],result['temp1'],result['temp2'])
		print str_temp
	except:
		print '查询失败'
else:
	print '没有找到该城市'
