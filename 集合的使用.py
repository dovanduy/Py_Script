# -*- coding: utf-8 -*-
# @Time    : 2018/10/28 17:09
# @Author  : chengz
# @File    : 集合的使用.py
# @Software: PyCharm

a = set('qqqqwertyuiop')
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
