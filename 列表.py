# coding:utf-8


li = [1, 2, 3, 4, 5]
print li.pop(li[2])
print li

# L.index(value, [start, [stop]]) -> integer -- return first index of value.
#     Raises ValueError if the value is not present.
# li = [1, 2, 3, 4, 5]
# x = li.index(4)
# print x

# li = "cheng zheng is ge hao haizi"
# sub = "is"
# print li.find(sub)

# # ------------------s = "aa bb cc aa dd ee aa ff"-------------------------------------------------------------
# # 1、求有多少个aa,其位置
# s = "aa bb cc aa dd ee aa ff"
# sub = "aa"
#
# def fincount(s,sub):
# 	i = 0
# 	c = 0
# 	while i < len(s)-len(sub):
# 		if s[i:i+len(sub)] == sub:
# 			c += 1
# 		i += 1
# 	return c
#
# def finds(s, sub):
# 	i = 0
# 	li = list()
# 	while i < len(s)-len(sub):
# 		if s[i:i+len(sub)] == sub:
# 			li.append(i)
# 		i += 1
# 	return li
# cc = fincount(s, sub)
# print cc
# x = finds(s, sub)
# print x

# ---------------------------------------------------------
# s = [1, 62, 2, 9, 3, 6, 4, 0]
# # s.sort()
# # print s
# a = s[0]
# for i in s:
# 	if i < a:
# 		a = i
# 		s[s.index(i)] = a
# print s

# s = [1, 62, 2, 9, 3, 6, 4, 0]
# s.sort()
# print s[0], s[len(s)-1]

# def add(*a):
# 	s = 0
# 	for i in a:
# 		s += i
# 	return s
# x = add(1, 2, 3, 4, 5, 6, 7, 8, 9)
# print x

# ----------------------------------------
li = [1, 2, 3, 1, 2, 2, 3, 4, 5, 2, 1, 3, 3, 2, 14, 5, 3, 3, 2, 1, 1, 3]
# print li
# pf = li.index(li[0])
# pp = li.index(li[0], pf+1)
i = 0
s = li.count(2)
while i < s:
    li.pop(li.index(2))  # 移除所有的2
    i += 1
    print li
# print 'pf', pf
# print 'pp', pp

# li = range(1,50)
#
# print li
# # print li[li.index(22):li.index(33)]
# # print li.index(33)

# li = [1, 2, 3, 1, 2, 3, 4, 5, 2, 1, 3, 3, 2, 14, 5, 3, 3, 2, 1, 1, 3]
# print li
#
# pf = li.index(li[0])
# if li.count(li[0]) > 1:
# 	pp = li.index(li[0], pf+1)
# 	print pp
# 	li.pop(pp)
# 	print li
# =====================================
# 用列表推导式生成100内的大于20的偶数
print [x for x in range(1, 100) if x > 20 and x % 2 == 0]

a = [1, 2, 3]
b = [4, 5, 6]
c = a
for i in b:
    c.append(i)
print c

d = [4, 5, 6]
e = d
d.append(7)  # e也会随之改变
print e
del d
print e

li = [1, 21, 3, 1, 2, 3, 4, 5, 2, 1, 3, 3, 2, 14, 5, 3, 3, 2, 1, 1, 3]
lt = list(set(li))
print lt

li = [1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 3, 5, 88]
li2 = []
for i in li:
    if i not in li2:
        li2.append(i)
print li2