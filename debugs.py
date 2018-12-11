# coding:utf-8
import os


# 列出某个文件夹下的所有 case,这里用的是 python， 所在 py 文件运行一次后会生成一个 pyc的副本
# caselist = os.listdir('E:\\cz\\Sele_Test\\baidu\\test_case')

# print caselist

# for li in caselist:
#     s = li.split('.')
# s1 = li.split('.')[1:][0]
# print s,
# print '\n'
# print s1
def fun(self, x):
    print "==x==", repr(x), 'is', len(x)


class My(object):
    def __init__(self):
        self.name = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        print self.name


if __name__ == '__main__':
    a = My()
    a.set_name('cz1')
    a.get_name()
    b=My()
    b.set_name('cz2')
    b.get_name()
    a.get_name()
