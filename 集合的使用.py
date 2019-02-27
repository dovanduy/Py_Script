# -*- coding: utf-8 -*-
# @Time    : 2018/10/28 17:09
# @Author  : chengz
# @File    : 集合的使用.py
# @Software: PyCharm

"""集合最好的应用是去重。集合没有特殊的表示方法，而是通过一个set函数转换成集合"""
a = set('qwerty')
b = set("poiu")
# 判断集合的所有元素是否都包含在指定集合中   是否为子集
print a.issubset(b), b.issubset(a)

s = 'az'
# 改  使用自身和其他集合的并集更新集合 可迭代的值都可以
a.update(s)
print "update=>>>", a

# 增
a.add('66a')
print 'add=>>>', a

# 去掉包含集合st中的元素  差集
st = {'e', 'i', 'o', 'q', 'p'}
print '差集=>>>', a.difference(st)
print '差集=>>>', a - st

# 并集
print '并集=>>>', a.union(b)
print '并集=>>>', a | b

# 交集
print "交集=>>>", a.intersection(b)
print "交集=>>>", a & b

# 交叉补集   不是相同的元素
print "交叉补集=>>>", a.symmetric_difference(b)
print "交叉补集=>>>", a ^ b

# 随机删除元素，并不是删除第一个
print a.pop()
print 'pop=>>>', a

# 指定删除  删除不存在的元素会报错
a.remove('o')
print 'a=>>>', a

# 同remove，删除不存在的元素时不会报错
a.discard('o')
print 'a=>>>', a

# 清空
a.clear()
print 'a=>>>', a

# 不可变集合
a = frozenset("hello")
print a

sets = {1, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4}
print list(sets)
