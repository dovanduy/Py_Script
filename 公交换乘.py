# coding:utf-8
# 目标：从cc 坐车到 dd  ,要转车，先要找到转换站点，然后起点到转，转到终点
a10 = "aa bb cc ee ff gg jj"
b20 = "qq ww tt xx gg vv pp oo dd hh mm"
a11 = a10.split()
b21 = b20.split()
# print a11
# print b21
st = "cc"
ed = "dd"
# 找中转点
for i in a11:
	if i in b21:
		za11 = a11.index(i)
		zb21 = b21.index(i)
		# print za11, zb21
# 找起点
s = 0
for i in a11:
	# s += 1
	if i == st:
		sst = a11.index(i)
	# print sst
# else:
# 	print "起点不在该路线内！！！"
	# break
# 找终点
d = 0
for i in b21:
	# d += 1
	if i == ed:
		sed = b21.index(ed)
# else:
# 	print "终点不在该路线内！！！"
	# break

for k in a11[sst:za11+1]:
	print k, '->',
print
for x in b21[zb21:sed+1]:
	print x, '->',