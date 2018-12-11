# -*- coding: utf-8 -*-
# @Time    : 2018/11/3 12:26
# @Author  : chengz
# @File    : 异常处理.py
# @Software: PyCharm


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division␣by␣zero!")
    except TypeError:
        print("typeerror")
    else:
        print "result_is", result
    finally:
        print("executing␣finally␣clause")


divide(2, 1)
divide('2', '1')
