#coding:utf-8
import re
import urllib2

strs='imooc python'

print strs.find('ll')

pa= re.compile(r'imooc')
ma=pa.match(strs)
print ma

print ma.group()

###怕图片

url="http://www.imooc.com/course/list"

req=urllib2.urlopen(url)
urllist=req.read()

lis=re.findall(r'http:.+\.jpg',urllist)
print lis
i=0
for url in lis:
    f=open(str(i)+'.jpg','w')
    req=urllib2.urlopen(url)
    buf=req.read()
    f.write(buf)
    i+=1

print "ok"

str =''' TOUCH|{'x':443,'y':981,'type':'downAndUp',}TOUCH|{'x':618,'y':1213,'type':'downAndUp',}TOUCH|{'x':256,'y':200,'type':'downAndUp',}
TOUCH|{'x':45,'y':82,'type':'downAndUp',}
TOUCH|{'x':94,'y':1202,'type':'downAndUp',}
TOUCH|{'x':634,'y':1221,'type':'downAndUp',}
TOUCH|{'x':234,'y':893,'type':'downAndUp',}
TOUCH|{'x':351,'y':1053,'type':'downAndUp',}'''

pattern = re.compile(r'\d+')
res = pattern.findall(str)
print res