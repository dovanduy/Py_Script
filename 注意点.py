# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 20:19
# @Author  : chengz
# @File    : 注意点.py
# @Software: PyCharm


"""重要警告: 默认参数的值只会被求一次值. 这使得当默认参数的值是可
变对象时会有所不同, 如列表, 字典, 或大多类的对象时。
如果你不想让参数值被后来的调用共享,就li=None，每次都判断下li是否为None
例如, 下面的函式在随后的调用中会累积参数值:"""


# 每次都会重置li的值
def lts(a=0, li=None):
    if li is None:
        li = []
    li.append(a)
    # print a,li
    return li


# li的值会一直共享
def lists(a=0, li=[]):
    li.append(a)
    # print a,li
    return li


#  *arg 之后的形式参数只能是关键字参数a=1
def f(e, *arg, **dt):
    print e
    print arg
    print dt


def foo(num):
    """异常处理"""
    try:
        hh = float(num)
        return hh
    except TypeError, q:
        print 'q:', q

    except ValueError, x:
        print 'x:', x
    except BaseException, p:  # 包含所有的错误
        print 'p:', p

    finally:
        print "wo lai le !!!"


if __name__ == '__main__':
    li1 = lists(1)
    print li1
    li2 = lists(2)
    print li2

    f(1, 2, 3, 4, 5, a=1, b=2, c=3)

    str =u"你就是"

    for i in str:
        print ord(i),

    print foo('g')

    ls = "qwertyuiop"
    la = ""
    print ls
    for i in range(1, len(ls) + 1):
        la += ls[-i]
    print la
    # 切片方式
    print ls[::-1]
