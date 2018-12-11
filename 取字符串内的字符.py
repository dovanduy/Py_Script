import requests
import re
i=0
s = "welcome to visit my websit http://www.baidu.com hehe http://www.163.com hehe http://www.souhu.com hehe!!!"

html = re.findall('http://.*?.com',s,re.S)

for i in html:
	print i







# head = "http"
# tail = ".com"
# i =0
# ph=0
# pt=0
# pre=0
# while i<=len(s)-len(head):
# 	j=0
# 	c=0
# 	while j<len(head):
# 		if s[i+j] == head[j]:
# 			c+=1
# 		j+=1
# 	if c==len(head):
# 		ph=i
# 		print "ph =",ph,
# 	j=0
# 	c=0
# 	while j<len(tail):
# 		if s[i+j] == tail[j]:
# 			c+=1
# 		j+=1
# 	if c==len(tail):
# 		pt=i
# 		print "pt =",pt,
# 		if ph<pt and pre!=ph:
# 			k=ph
# 			dns=""
# 			while k<pt+len(tail):
# 				dns+=s[k]
# 				k+=1
# 				pre=ph
# 			print dns
# 	i+=1
