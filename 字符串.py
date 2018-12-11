# coding:utf-8
# import  random
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
s = "chegn zheng is ge hao hai zi "
sub = "eu"
def myfind(s, sub):
	i = 0
	while i <= len(s)-len(sub):
		if s[i:i+len(sub)] == sub:
			print "find",sub,i
			break
		i += 1
	else:     #当循环结束时执行
		print -1
myfind(s,sub)