# coding:utf-8

# s1 = dict(a=1, b=2, c=3)
# s2 = dict(a=7, w=7, b=9)
# s3 = s1.keys()
# s4 = s2.keys()
# s6 = set(s3)
# s7 = set(s4)
# l1 = list()
# for i in s3:
# 	if i in s4:
# 		l1.append(i)
# print l1
#
# s5 = s6.intersection(s7)
# print s5

# l1 = [1,2,3,4,5,6,7,8,9]
# l2 = [111,22,33,44,55,3,4,5]
# s1set = set(l1)
# s2set = set(l2)
# print s1set
# print s2set
#
# # l4 = list(s1set.difference(s2set))
# #
# # l5 = list(s2set.difference(s1set))
# #
# # l6 = list(s2set.intersection(s1set))
# #
# # l = (l4+l5+l6)
# # print l
# l3 = []
# for i in l1:
# 	if i not in l3:
# 		l3.append(i)
# for i in l2:
# 	if i not in l3:
# 		l3.append(i)
# print l3
# -----------------------------

# 算出两个列表中的并集和交集
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ab = [0, 1, 2, 3, 4]

c1 = set(a)
c2 = set(ab)

c3 = c1 & c2  # 交集
c4 = c1 | c2  # 并集

# print list(c3)
# print list(c4)
