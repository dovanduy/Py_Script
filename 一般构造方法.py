# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 15:52
# @Author  : chengz
# @File    : 一般构造方法.py
# @Software: PyCharm


class Briad(object):
    def __init__(self):
        self.hungrg = True
        print 111

    def eat(self):
        if self.hungrg:
            print 666
            self.hungrg = False
        else:
            print 999


class SongBrid(Briad):
    def __init__(self):
        # Briad.__init__(self)
        super(SongBrid, self).__init__()
        self.sound = True
        print 222

    def sing(self):
        print self.sound


s = SongBrid()
s.sing()
s.eat()
