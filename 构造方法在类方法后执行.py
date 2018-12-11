# -*- coding: utf-8 -*-
# @Time    : 2018/6/21 15:17
# @Author  : chengz
# @File    : 构造方法在类方法后执行.py
# @Software: PyCharm


class MyClass(object):
    msg = "=========="

    @classmethod
    def createObj(cls, name, color):
        print "obj will be created:%s(%s,%s)" % (cls.__name__, name, color)
        return cls()

    @staticmethod
    def printMsg():
        print MyClass.msg

    def __init__(self, name="cz", color="pink"):
        self.name = name
        self.color = color
        print "gou zao mth:", name, " ", color


MyClass.printMsg()

ins = MyClass.createObj("aa", "bb")
print ins.msg

print ins.name
del ins
