# coding:utf-8
s = "aa bb cc dd ee ff gg"
ls = s.split(' ')
print ls
# for i in ls:
# 	print i,
# print ls[-1]

print tuple(s)   #yuan zu



# import urllib
# import urllib2
# temp = "//img11.360buyimg.com/n5/jfs/t1495/232/620266644/335351/34089cdf/559fc87dN509fcf49.jpg"
# # temp = "//gd1.alicdn.com/bao/uploaded/i1/200906269/TB2MfcIcFXXXXXnXXXXXXXXXXXX_!!200906269.jpg"
# h = "//img"
# t = ".jpg"
# url = raw_input("url:")
# up = urllib2.urlopen(url)
# # print up
# s = up.read()
# print s
# posh = -len(h)
# post = -len(t)
# # 呵呵
# i = 0
# while i < s.count(h):
# 	posh = s.find(h, post+len(h))    #函数原型：find(str, pos_start, pos_end)
# 	post = s.find(t, posh+len(h))
# 	a = s[posh:post + len(t)]
# 	http = a.find("http")
# 	# if len(s[posh:post+len(t)]) == len(temp):
# 	# print s[posh:post+len(t)]
# 	# 	url = a[http:]
# 	# 	urllib.urlretrieve(url,str(i)+ '.jpg')
# 	i+=1
