# coding:utf-8
s = "http://www.baidu.com http://www.uuse123c.com http://www.ur123.com"
h = "http"
t = ".com"
posh = -len(h)
post = -len(t)
# 呵呵
i = 0
while i < s.count(h):
    posh = s.find(h, post + len(h))
    post = s.find(t, posh + len(t))
    i += 1
    print posh, post, '\t', s[posh:post + len(h)]

print "====================="
s = "httpfhdjkjjjjjjjjjjj.comgghttpfffff.com"
h = "http"
t = ".com"
posh = -len(h)
post = -len(t)
i = 0
while i < s.count(h):
    posh = s.find(h, posh + len(h))
    print i
    i += 1

# import re

#
# secret_code = 'http://www.wwwbaiducomhttp.com http://www.uuse123.com http://www.ur123.com'
#
# d = re.findall('http.*?com', secret_code)
# # print d
# for each in d:
# 	print each
