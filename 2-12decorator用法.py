# coding:utf-8
import time


def log(f):
    def fn(x):
        print 'call' + f.__name__ + '()...'
        return f(x)

    return fn


@log
def factoria(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print factoria(10)


def per(f):
    def ad(*args, **kw):
        t1 = time.time()
        time.sleep(1)
        r = f(*args, **kw)
        t2 = time.time()
        print 'call %s() in %fs' % (f.__name__, (t2 - t1))
        return r

    return ad


@per
def factorial(n, m):
    return n + m


print factorial(10)
