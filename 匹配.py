#coding:utf-8
import re
from re import findall,search,S
# text = "Hi, I am Shirley Hilton. I am his wife."
# # text = "site sea sue sweet see case sse ssee loses"
# # m = re.findall(r"\bhi\b", text)  #“\b”在正则表达式中表示单词的开头或结尾
# # m = re.findall(r"hi", text)
# # m = re.findall(r"i.", text)
# # m = re.findall(r".", text)  #“.”类似的一个符号是“\S”，它表示的是不是空白符的任意字符
# # m = re.findall(r"i.*e", text)  #“*”在匹配时，会匹配尽可能长的结果。
# m = re.findall(r"i.*?e", text)   #想让他匹配到最短的就停止，需要用“.*?”
# if m:
#     print m
# else:
#     print 'not match'
#

# ----------------------------------------
# a = 'cz:123,cs:345'
# b = re.findall(r'c.',a)     # 点号的使用
# print b
# ------------------------------
# a = "hello world"
# b = re.findall(r'l*',a)     # *号的使用
# print b
# ---------------------------------------
# a = "hello world"
# b = re.findall(r'l?',a)     # ?号的使用
# print b
# -----------------------------------------
secret_code = 'hadkfalifexxIxxfasdjifja134xxlovexx23345sdfxxyouxx8dfse'
#.*的使用举例
# b = re.findall('xx.*xx',secret_code)
# print b
# -------------------------------------------
# #.*？的使用举例
# c = re.findall('xx.*?xx',secret_code)
# print c
# -----------------------------------
# #使用括号与不使用括号的差别
# d = re.findall('xx(.*?)xx',secret_code)
# print d
# for each in d:
#     print each
# --------------------------------------
# s = '''sdfxxhello
# xxfsdfxxworldxxasdf'''
#
# d = re.findall('xx(.*?)xx',s,re.S)
# print d

# ------------------------------------
#对比findall与search的区别
# s2 = 'asdfxxIxx123xxlovexxdfd'
# # f = re.search('xx(.*?)xx123xx(.*?)xx',s2).group(2)
# # print f
# f2 = re.findall('xx(.*?)xx123xx(.*?)xx',s2)
# print f2[0][1]
# --------------------------
#


#sub的使用举例
# s = '123rrrrr123'
# output = re.sub('123(.*?)123','123%d123'%789,s)
# print output
# ------------------------------
#演示不同的导入方法     shaoyong
# info = findall('xx(.*?)xx',secret_code,S)
# for each in info:
#     print each

#不要使用compile
# pattern = 'xx(.*?)xx'
# new_pattern = re.compile(pattern,re.S)
# output = re.findall(new_pattern,secret_code)
# print output

#匹配数字
a = "TOUCH|{'x':351,'y':1053,'type':'downAndUp',}TOUCH|{'x':51,'y':1053,'type':'downAndUp',}TOUCH|{'x':451,'y':1053,'type':'downAndUp',}"
b = re.findall('(\d+)',a)
# print b
i = 0
for i in range(0,5,2):
	print b[i]+','+b[i+1]
	# print i
