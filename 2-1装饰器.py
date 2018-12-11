# coding:utf-8

import time


def fun1(f):
    print fun1.__name__

    def fun2(x):
        time.sleep(1)
        print fun2.__name__
        print f, x

    return fun2


f1 = fun1(666)
f1(2)


#####闭包#####

def set_passline(passline):
    def cmp(val):
        if val >= passline:
            print "pass"
        else:
            print "failed"

    return cmp


f_150 = set_passline(90)
f_100 = set_passline(60)

f_150(89)
f_150(90)
f_100(61)
f_100(59)

print "===================定制求和======================"


def my_sum(*arg):
    return sum(arg)


def dec(func):
    def in_dec(*arg):

        if len(arg) == 0:
            return 0
        # 元组改不了值，就这样返回0了
        for val in arg:
            if not isinstance(val, int):
                return 0
        return func(*arg)

    return in_dec


my_sum = dec(my_sum)

print my_sum(1, 2, 3, 4, 5)

print my_sum(1, 2, 3, 4, 5, 'a')  # 有其他字符  为0

print my_sum()
