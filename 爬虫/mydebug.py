# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 9:19
# @Author  : chengz
# @File    : mydebug.py
# @Software: PyCharm

all_title = []

olds = [1, 2, 3, 4, 5]
for i in olds:
    mynews = {}
    mynews['news'] = i
    all_title.append(mynews)

print all_title
