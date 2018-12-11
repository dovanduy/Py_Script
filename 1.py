# coding:utf-8
import string
import re
import os
import glob

li = [5, 6, 4]

# 迭代问题，输出可迭代的元素
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = []
for i in L1:
    if isinstance(i, str):
        L2.append(i)
print L2


# 快速生成列表
print [x * x for x in range(1, 11)]


# 杨辉三角
def triangles(count):
    i = 0
    l = [1]
    while (i < count):
        yield l
        l = [1] + [l[j] + l[j + 1] for j in range(i)] + [1]
        i += 1


print list(map(str, [1, 2, 3, 4, 5, 6, 7, 8]))
# =========================================
print sorted(['wew', 'SD', 'ff', 'wer'], key=str.lower, reverse=True)


# 按照名字进行排序

def stuSortByName(item):
    return item[0]


def stuSortByGrade(item):
    return item[1]


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(list(sorted(L, key=stuSortByName)))
print(list(sorted(L, key=stuSortByGrade, reverse=True)))


def sums(*args):
    def sum():
        a = 0
        for i in args:
            a = a + i
        return a

    return sum


f = sums(1, 2, 3, 4)

print f
print f()

print list(map(lambda x: x * x, [1, 2, 3, 4, 5]))


# ================“装饰器”（Decorator）==========================

def log(funs):
    def wapper(*args, **kwargs):
        print "call %s()" % (funs.__name__)
        return funs(*args, **kwargs)

    return wapper


@log
def hh():
    print 12345


hh()

print isinstance((1, 2, 3), (list, tuple))

# 神奇的方法,打印字典的值

dicts = {"name": 12, "age": 23}

print "处理结果:%(name)s,%(age)s" % (dicts)

a = open("a.txt", 'w')

a.write("12345678")
a.close()
a = open("a.txt", 'r')
print a.read(88)
# 游标
a.seek(0)
print a.read(1)

print "处理结果:{1},{0}".format("dicts", "fgd")
print "处理结果:{one},{zero}".format(zero="dicts", one="fgd")

# 1. 已知字符串 a = "aAsmr3idd4bgs7Dlsf9eAF",要求如下
a = "aAsmr3idd4bgs7Dlsf9eAF"
# 1.1 请将a字符串的大写改为小写，小写改为大写。
print a.swapcase()
# 1.2 请将a字符串的数字取出，并输出成一个新的字符串。
s = re.findall("\d+", a)
print ''.join(s)
print ''.join([s for s in a if s.isdigit()])

# 1.3 请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}
s = a.lower()
x = {}
for i in set(s):
    x[i] = s.count(i)
print x

# 1.4 请去除a字符串多次出现的字母，仅留最先出现的一个。例 'abcabb'，经过去除后，输出 'abc'
# s=''.join(re.findall("\D+", a))
aa = list(a)
a_s = list(set(aa))
a_s.sort(key=aa.index)
print " ".join(a_s)

# 1.5 请将a字符串反转并输出。例：'abc'的反转是'cba'
print a[::-1]


# 1.6 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符 串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）
# 1.7 请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
# 1.8 要求如1.7，此时的单词判断，由'boy'改为四个，分别是 'boy','girl','bird','dirty'，请判断如上这4个字符串里的每个字母，是否都出现在a字符串里。
# 1.9 输出a字符串出现频率最高的字母

##########参数事宜
def Fundemo(*a, **b):
    return a, b


# 未赋值的参数全部给*a；；赋值的参数全部给**b
print Fundemo(1, 2, 3, 4, [1, 2, 3], a=1, b=2, c=3)


####################################

# 求最大数a = 123 b = 345 c = 444

def maxNum(**kw):
    d = {}
    for k, v in kw.items():
        d[k] = v
        li.append(v)

    li.sort()
    s = sorted(d.iteritems(), key=lambda asd: asd[1])[-1]
    return s[0]


print maxNum(a=123, b=345, c=444)


class Parent(object):

    def altered(self):
        print "PARENT altered()"


class Child(Parent):
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"


dad = Parent()
son = Child()

dad.altered()
son.altered()


def fab(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b


for i in fab(20):
    print i, "\b,",

print ""
# 当前工作目录
print os.getcwd()
print glob.glob(os.getcwd()+'/*.py')

import logging
logging.info('Informational␣message')
