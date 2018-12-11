# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 10:12
# @Author  : chengz
# @File    : 类相关.py
# @Software: PyCharm


class Per(object):
    num = 0

    def init(self):
        Per.num += 1

    def __wb(self):
        print 66666

    def setname(self, name):
        self.name = name

    def getname(self):
        self.__wb()
        return self.name

    def talk(self):
        print "Per 里面的方法"


class Dog(object):

    def talk(self):
        print "Dog里面的方法"


class Dd(Per):
    def age(self):
        pass


class Parent(Per,Dog):
    pass


p = Dd()
p.setname('chengz')
print p.getname()

p.init()

d = Per()
d.init()    # 会累加

d.num = "asd"   # 相当于一个局部变量

print d.num
print p.num
print "=====同时继承两个类===="

tk=Parent()
tk.talk()  # 继承多个类时，先继承的类中的方法会重写后继承类中的方法