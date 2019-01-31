# -*- coding: utf-8 -*-
# @Time    : 2018/10/28 17:09
# @Author  : chengz
# @File    : 集合的使用.py
# @Software: PyCharm

"""集合最好的应用是去重。集合没有特殊的表示方法，而是通过一个set函数转换成集合"""
a = set('qqqqwertyuiop')
b = set("poiu")
print a.issubset(b)
s = 'az'
# 改
a.update(s)
print a

# 增
a.add('66a')
print a

# 删除第一个
print a.pop()
print a

# 去掉包含集合st中的元素
st = "eioqp"
print a.difference(st)

# 清空
a.clear()
print a

print set([1, 2, 3, 4])
sets = set([1, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4])
print list(sets)
