# coding:utf-8
from types import MethodType


class Animal(object):
    def __init__(self):
        pass

    def runs(self):
        print "run is %s()" % Animal.__name__


class Dog(Animal):
    def __int__(self):
        # Animal.__init__(self)
        super(Dog, self).__init__()

    def runs(self):
        print "run is %s() " % Dog.__name__


# 只要传入的对象有run()方法就行了
def run_twice(animal):
    animal.runs()


run_twice(Animal())
run_twice(Dog())

print type(run_twice)
print type(Animal())


# ==============给类动态添加属性================
class Test(object):
    def __init__(self, name):
        self.name = name


def fun(self, age):
    self.age = age


s = Test("cheng")
s.fun = MethodType(fun, s)
s.fun(26)
# 该方法只是在s实例中使用
# 如果让所有实例都能使用则Test.fun=fun；可以直接在类中定义该方法
print s.name
s.name = "zheng"
print s.name

import re

s = "订单总数：18"
dd = re.findall("\d+", s)
print dd

print("=======分界线=========")


class CallFun(object):

    def __init__(self, name):
        print "__init__"
        self.name = name

    # def __call__(self, name):
    #     print "__call__"
    #     return self.runs(name)

    def runs(self):
        # self.name = 1 / 0
        print "runs调用了", self.name

    def __enter__(self):
        print "__enter__"
        return self

    def __del__(self):
        print "__del__"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print '__exit__'
        print "exc_type=>>>", exc_type
        print "exc_val=>>>", exc_val
        print "exc_tb=>>>", exc_tb


def calls(name):
    return CallFun(name)


# with CallFun("cheng1") as call:
#     call.runs("cheng2")

with calls("cz9025") as call:
    call.runs()

"""
with:
__enter__方法是with开始运行时触发此方法运行
__exit__当with运行结束后触发此方法运行
"""


class Member(object):
    num = 0

    def init(self):
        Member.num += 1


n = Member()
n.init()
print Member.num
m = Member()
m.init()
print Member.num
