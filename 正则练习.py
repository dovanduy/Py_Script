# coding:utf-8

import re

strs = "http://www.baidu.com http:/2312/www.baidu.com"

print "非贪婪匹配"
ls = re.findall(r'www.*?\.com', strs)
print ls

print "匹配字符集，默认单个匹配，后面最好加次数+"
ls = re.findall(r'[bai]+', strs)
print ls

print "匹配纯数字"
ls = re.findall(r'\d+', strs)
print ls

print "+匹配"
ls = re.findall(r'w+', strs)
print ls

print "匹配指定次数的数字"
ls = re.findall(r'\d{1,4}', strs)
print ls

print "匹配字符串字符开头"
ls = re.findall(r'^h.+', strs)
print ls

print "匹配字符串字符结尾"
ls = re.findall(r'.+om$', strs)
print ls

print "指定的字符串匹配必须在开头/结尾"
ls = re.findall(r'\Ah.+', strs)
print ls

print "匹配左右任意一个表达式"
ls = re.findall(r'\Ah\w+|\d+|\d{22}', strs)
print ls

print "括号中表达式作为一个分组"
ls = re.findall(r'www.\w+\.com', strs)
print ls
