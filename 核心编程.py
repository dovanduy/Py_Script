# coding:utf-8
# from types import IntType
# a = 1
# b = type(a)
# print b
# c = int
# print c
# if b == c:
#     print 12
# else:
#     print 23
#
# print '-------------------'
# if type(a) is IntType:
#     print 1
#
# if isinstance(a, int):
#     print 1
#
# q = 1.0
# print id(q)
# p = 1.0
# print id(p)
# print q is p
# if q is p:
#     print "true"
# print "----------------------"
# a = 1
# del a
# print a
# print "--------------------------"
# b = 10000000000
# print repr(b)
#
# print 5//2
# print 5/2
# print 2**3
# print 2**-3
# print cmp(4, 4)  #比较两个数的大小，x大于y，则输出为正数，x小于y，输出为负数，当X = Y，输出为0
#
# s = str(123)
# print type(s),repr(s)
#
# q = complex(1, 2)   #转化为复数
# print q

# import math
# s = 2
# print math.pi,math.e
# print "------------------------------------------------"
# 一个闰年就是指它可以被 4 整除，但不能被 100 整除；或者它既可以被4又可以被100整除
# year = input("please input year:\n")
#
# # s = repr(year)
# # print s
# # temp = int
# # print type(year)
# if 1000 < year < 9999:
# 	if year%4 == 0 and year%100 != 0 or year%4 == 0 and year%100 == 0:
# 		print "it's yun nian"
# 	else:
# 		print "it's not yun nian"
# else:
# 	print "input error!!!"
# print "------------------------------------------"
# print 012+2
# print 0xf
# print "------------------------------------"

# ls = [1,45,67,32,7,23,888,90,35]
# mx = max(ls)
# print mx,ls.index(mx)
# mi = min(ls)
# print mi,ls.index(mi)
# print sum(ls)
# print "--------------------"
# s = "abcdefghijklmnopqrstuvwxyz"
# a = s[1:6]
# b = s[20:]
# s = a+b
# print s,
# print "----------------------------------"
# s = "abcdefg"
# for k, v in enumerate(s):
# 	print k,v
#
# t = "qwertyu"
# print zip(s,t)
# print "----------------------"
# print unichr(12345)
# print ord(u'\u1234')
# print "--------------------------"
# 判断字符串是否以指定字符结束
# string = u"abcdefg"
# print string.endswith('g',0,len(string))  #后面2个参数为起始位置
# '''
# string.find(str, beg=0,end=len(string))    检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，
# 则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
# '''
# '''string.isdigit()   如果 string 只包含数字则返回 True 否则返回 False'''
# string.lstrip() #截掉 string 左边的空格
# string.rstrip()  #截掉 string 右边的空格
# print "----------------------------------"
# s = ['They', 'stamp', 'them', 'when', "they're", 'small']
# for i in reversed(s):
# 	print i,
# print
# print sorted(s)
# ls = [1,5,4,3,2]
# ls.sort()
# print ls
# '----------------------------------------'
# print "-"*15,"创建字典新方法","-"*15
# ddict = {}.fromkeys(('x', 'y'), -1)   #值可以为空
# print ddict         #{'y': -1, 'x': -1}

"--------------------------------------------------"
# dict2 = {'name': 'earth', 'port': 80}
# for key in dict2:
# 	print 'key=%s, value=%s' % (key, dict2[key])
"------------------字符串转字典--------------------------------"
# s1 = "abcdefg"
# s2 = "qwertrt"
# dd = dict(zip(s1, s2))
# print dd
# dict9 = dict(**dd)
# print dict9
# di = dict9.copy()
# print di
"--------------------------------------------------"
# a = hash(s1)
# print a
"------------------------------------------------"
# with open("a.txt",'r') as f:
# 	for i in f:
# 		print i,
"-------------------------------------------"
# raise [SomeException [, args [, traceback]]]
# assert 1 == 0
"-----------------------------------------------"
# try:
# 	assert 1 == 0, 'One does not equal zero silly!'
# except AssertionError, args:
# 	print '%s: %s' % (args.__class__.__name__, args)

	# try:
	# 	print
	# except AttributeError:
	# 	print
"------------------------------------------------"
# try:
# 	s = input("")
# except BaseException:
# 	print "999999999",
"----------------函数名也可以作为一个参数传递--------------------------"
# def foo():
# 	return "wo shi yi ge hao hai zi "
#
# def bar(arg):
# 	return arg()
#
# print bar(foo)
#
# a = foo
# print a()
"-----------------------------------------"
# add = lambda x, y : x+y
# a = add(1,2)
# print a
"----------------------------------------------"
# from random import randint
# def odd(n):
# 	return n % 2
# allnums = []
# for each in range(9):
# 	allnums.append(randint(1, 99))
# 	print allnums
# 	print filter(odd, allnums)   #每个 filter 返回的非零（true)值元素添加到一个列表中
"----------------------------------------------------"
def func(x,y):
	return x + y
# a = func(func(1,2),3)
# print a
a = reduce(func, [1, 2, 3])
print a

"--------------------------------"
