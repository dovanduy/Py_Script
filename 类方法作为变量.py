# -*- coding: utf-8 -*-
# @Time    : 2018/10/19 21:39
# @Author  : chengz
# @File    : 类方法作为变量.py
# @Software: PyCharm


class Father(object):
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def __call__(self, args):
        print 'call=>', args


class Son(object):
    def __init__(self, like=None, have=None, width=None, height=None):
        self.like = like
        self.have = have
        self._width = width
        self._height = height
        self.father = Father(self.like)

    def run(self):
        print self.like, self.have


if __name__ == '__main__':
    son = Son(width=666)
    son.like = "eat"
    son.have = "fast"
    son.run()

    son.like = "ch"
    son.have = "zh"
    son.run()
    # son.cat()
    son.father(56)

    fa = Father("ch", 28)
    fa(666)
