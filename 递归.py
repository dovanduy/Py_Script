# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 16:30
# @Author  : chengz
# @File    : 递归.py
# @Software: PyCharm


def fn(n):
    """10的阶乘"""
    if n > 1:
        return n * fn(n - 1)
    else:
        return 1


print fn(10)
