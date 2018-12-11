# coding:utf-8

def add(x, y):
    def a():
        return x + y

    return a


b = add(2, 3)

print b()
