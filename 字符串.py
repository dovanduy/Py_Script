# coding:utf-8
import re
import random

# i = 0
#
# while i<20:
# 	x = random.randint(100000,1000000)
# 	s = str(x)
# 	if "4" in s or "7" in s:
# 		k=0
# 		while k< len(s):
# 			if s[k] == "4" or s[k] == "7":
# 				print s[k],k,
# 		k+=1
# 	i+=1
#
# i = 0
# while i<100:
# 	if i<10:
# 		print "nis sb00"+str(i)
# 	elif i<100:
# 		print "ni s sb0"+str(i)
# 	else:
# 		print "nis sb"+str(i)
# 	i+=1

# x=97
# i=0
#
# while i<26:
# 	s = chr(x+i)
# 	if i<9:
# 		li = s+str(0)+str(i+1)
# 		print li,
# 	else:
# 		lis = s+str(i+1)
# 		print lis,
# 	i+=1


i = 0
s = "welcome to visit my websit http://www.baidu.com hehe http://www.163.com hehe http://www.souhu.com hehe!!!"

html = re.findall('http://.*?.com', s, re.S)

for i in html:
    print i

print "i am {0}, today {1} yesold, haha {2}".format('cz', 'yellow', '66')
print "i am {name}, today {ye} yesold, haha {he}".format(name='cz', ye='yellow', he='66')
print "i am {}, today {} yesold, haha {}".format('cz', 'yellow', '66')
# 索引
print "i am {2}, today {0} yesold, haha {1}".format('cz', 'yellow', '66')
# 指定类型
print "i am {:s}, today {:d} yesold, haha {:f}".format('cz', 66, 0.66)
# 传的是列表的话，前面加个*
print "i am {:s}, today {:d} yesold, haha {:f}".format(*['cz', 66, 0.66])
# 传的是字典的话，加2个*
print "i am {name:s}, today {age:d} yesold, haha {he:f}".format(**{'name': 'cz', 'age': 66, 'he': 0.68})
