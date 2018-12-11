# -*- coding: utf-8 -*-

# # 三个数字比大小
# print "请输入三个数字：\n"
# x = raw_input()
# y = raw_input()
# z = raw_input()
#
# max = x
# if y>max:
# 	max = y
# if z>max:
# 	max = z
# print max


# #输入一个年份，判断是否为闰年
# print "请输入一个年份：\n"
# year = input()
# if (year%400==0 or year%4==0 and year%100!=0):
# 	print year
# else:
# 	print "flase"

# # 输入一个分数判定成绩等级
# s = input()
# if s > 100:
# 	g = '牛逼'
# elif s>=90:
# 	g = 'A'
# elif s>=80:
# 	g = 'B'
# elif s>=60:
# 	g= 'C'
# else:
# 	g = '不及格'
# print g

# # 猜数游戏。预设一个0~9之间的整数
# from random import  randint
# num = randint(1,10)
# fige = False
# while fige ==  False:
# 	print '请输入一个数:\n'
# 	s = input()
# 	if s==num:
# 		print "your win!!!"
# 		fige = True
# 	if s>num:
# 		print "too big"
# 	if s<num:
# 		print "too small"

# 判断输入一个数字是否为素数
# import math
# n=int(input('请输入一个数：'))
# i=2
# while i <= int(math.sqrt(n)):
#     if n%i == 0:
#         print n,"不是素数！"
#         break
#     else:
#         i=i+1
# else:
#     print n,"是素数！"

# i = "abc qwe rty asd zxc vbnm yhn"
# j = "zxc"
# k=0
#
# while k<=len(i)-len(j):
# 	n=0
# 	c=0
# 	while n<len(j):
# 		if i[k+n] == j[n]:
# 			# print i[k+n],"ok"
# 			c+=1
# 		n+=1
# 	if c == len(j):
# 		print i[k],i[k+1],i[k+2],
# 	k+=1


# i = "abc zxcqwe rty asd zxc vbnm yhn"
# j = "zxc"
# k=0
# while k<len(i)-len(j)+1:
# 	if i[k:k+3] == j:
# 		print k,j
# 	k+=1


# s = "http://fhdjkjjjjjjjjjjj.comgghttp://fffff.com"
# h = "http"
# t = ".com"
# posh = -len(h)
# post = -len(t)
# i = 0
# while i < s.count(h):
#    posh = s.find(h,post+len(h))
#    post = s.find(t,posh+len(t))
#    print s[posh:post+len(t)]
#    i+=1

# s = "comhttp://fhdjkjjjjjjjjjjj.comgghttp://fffff.httpcom"
# d = "httpcom"
#
# p = 0
# t = 0
# i = 0
# while i < len(s):
# 	if s[i] not in d:
# 		p = i
# 		break
# 	i +=1
# print s[p:]
# i = len(s)-1
# while i>=0:
# 	if s[i] not in d:
# 		t = i
# 		break
# 	i-=1
# print s[:t]
# print s[p:t]

# s = "        comhttp://fhdjkjjjjjjjjjjj.comgghttp://fffff.httpcom         "
# d = "com"
# a = ""
# # a = s.replace("com","COM")
# # print a
# a = "o"+s.strip()
# print a





# class thing(object):
# 	def __init__(self):
# 		self.num = 0
# 	def modu(self,nu):
# 		self.num +=nu
# 		return self.num
#
# a = thing()
# b = thing()
#
# print a.modu(20)
# print b.modu(30)
#
# print a.num
# print b.num

# # 完数
# m = 1000
# for a in range(2,m+1):
# 	s = a
# 	l1 = []
# 	for i in range(1,a):
# 		if a%i == 0:
# 			s -= i
# 			l1.append(i)
# 	if s == 0:
# 		print "完数: %3d, 因子包含:"%(a),
# 		print 1,"\t",
# 		for j in range(1,len(l1)):
# 			print "%d"%l1[j],"\t",
# 		print "\n"


# day=9
# x=1
# while day>0:
# 	x=(x+1)*2
# 	day-=1
# print "total =",x



# 向末尾添加l2
# i = 0
# while i< len(l2):
# 	l1.append(l2[i])
# 	i += 1
# print l1

# l1.extend(l2)
# print l1

# #删除列表里面的重复值，只保留一个
# l = [1,2,3,1,1,2,4]
# x = l.count(2)
# i = 0
# while i<x:
# 	l.remove(2)
# 	i+=1
# print l
#
# import requests
# s = requests.get('https://s.taobao.com/list?spm=a217f.7278617.a214d5w-static.3.qKuWZW&style=grid&seller_type=taobao&oeid=3587000&oeid=4561000&cps=yes&cat=51108009')
# print s.text
# s = "dfgdsg广东省佛山分公司的dsgdfg"
# w = open('a.txt','w')
# w.write(s)
# w.close()
# import urllib
# import urllib2
# temp = "//img11.360buyimg.com/n5/jfs/t1495/232/620266644/335351/34089cdf/559fc87dN509fcf49.jpg"
# temp = "https://g-search1.alicdn.com/img/bao/uploaded/i4/i3/TB1rZ0yIVXXXXb0XFXXXXXXXXXX_!!0-item_pic.jpg"
# h = "https://"
# t = ".jpg"
#
# posh = -len(h)
# post = -len(t)

# i = 0
# while i < s.count(h):
# 	posh = s.find(h,post+len(h))    #函数原型：find(str, pos_start, pos_end)
# 	post = s.find(t,posh+len(h))
# 	# a=s[posh:post+len(t)]
# 	if len(s[posh:post+len(t)]) == len(temp):
# 	# print s[posh:post+len(t)]
# 		url ='http:'+s[posh:post+len(t)]
# 		urllib.urlretrieve(url,str(i)+ '.jpg')
# 	i+=1
#

# #在定义的函数内使用全局变量，需要加上global
# def f(time):
# 	global c
# 	c+=1
# 	print c
# 	print time
# c = 0
# f(4)
# print "-------------"
# f(c+2)

# def delete(f):
# 	i = 0
# 	global s
# 	while i< len(s):
# 		if s[i] == f:
# 			# s.pop(s[i])
# 			s = s[:i]+s[i+1:]
# 			i-=1
# 		i += 1
#
# s = [0,5,5,5,5,5,1,2,3,5,5,5,4,5,6,7,8,9,90]
# delete(5)
# print s

# # 返回2个返回值
# x = 110
# y = 119
# print x,y
# def swap(a,b):
# 	return b,a
# x,y = swap(x,y)
# print x,y

# # def add(x):
# # 	return x+100
# def add(x,y=1):
# 	return x+y
#
# c = add(10)
# print c
#
# c = add(10,11)
# print c

# def findstr(s,sub,stat=0,ed=0):
# 	i = stat
# 	if ed == 0:
# 		ed = len(s)
# 	while i<=ed-len(sub):
# 		if s[i:i+len(sub)] == sub:
# 			print i
# 		i += 1
# s = "hello world im is xin lai de haha"
# sub = "l"
# findstr(s,sub,0,25)

# li = [1,2,3,4]    #函数作为形参
# def s(f,t):
# 	i = 0
# 	while i< len(t):
# 		t[i] = f(t[i])
# 		i += 1
# 	return t
#
# def f(x):
# 	return x + 5
# print li
#
# li = s(f,li)
# print li

# def p2(x,y,z):
# 	return x*y*z
# li = range(2,7)
# lt = range(3,8)
#
# l = map(p2,li,li,li) #两个列表也行
# print l

# 求一个列表的立方
# li = range(1,10)
# def pn(p, l, n):
# 	i = 0
# 	for x in l:
# 		l[i] = p(l[i], n)
# 		i += 1
# 	return l
# def p(n, m):
# 	# s = 1
# 	# for x in range(1, m+1):
# 	# 	s = s*n
# 	# return s
# 	return n**m
# li = pn(p, li, 3)
# print li

# import math
# li = [2,3,4,5]
# for i in li:
# 	print int(math.pow(i,3)),
# def f(x):
# 	return x**3
# lx = range(1, 10)
# ly = map(f, lx)
#
# lt = zip(lx, ly)
# print lt
# for i in lt:
# 	if i[0] == 4:
# 		print i[1]     #x[0]表示为x坐标，x[1]表示为y坐标
#
# print ord('a')   #字母转数字
#
# print chr(97)    #数字转字符
# -----------------------

#----------------------
# x, y = 4, 5
# small = x if x < y else y
# print small
# ---------------

#assert断言 当后面的条件为假时程序崩溃，并抛出AssertionError异常
# assert 3>4

# a = 'dsa'
# b = 'qwe'
# # c = True and a or b    #and or用法
# c = (1>4) and a or b
# print c

# from random import randint
# a = randint(1,12)
# print a


sub = "11aaaa22bb33cc44aa55ee"
s = "aa"
# print sub.find('aa')
# print sub.rfind("aa")
# print sub.count("a")
i = 0
pos = -2  #就是要查找的字串的长度
while i < sub.count("aa"):
	pos = sub.find(s, pos+len(s))
	print pos
	i += 1
