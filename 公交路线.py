# coding:utf-8
zhan = "aa bb cc dd ee ff gg hh ii jj"
site = zhan.split()
print site
ls = range(0, len(site)+1)
# print ls
q = zip(ls, site)
print 'q->', q
w = dict(q)
print w
s = "aa"
e = "ff"
st = ed = 0
for i in w.keys():
	if w[i] == s:
		st = i
	# else:
	# 	print "起点有误"
	# 	break
	if w[i] == e:
		ed = i
if st >= ed:
	print "您输入的站点有误!"
else:
	for v in w.values()[st:ed+1]:
		print v,
# print st, ed



