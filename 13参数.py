# coding:utf-8


def print_params(ag, *args):
    print ag, u"分割线1", args


print_params(1, 2, 'qw', 3, 4)
print_params(1, 2, 4)
print_params(1)


def print_params(**args):
    print u"分割线2", args


print_params(x=1, y=2, z=3)


def print_params(**args):
    print u"分割线2", args['a'], args['b']


ag = {'a': 1, 'b': 2}
print_params(**ag)


# 模拟range方法
def interval(start=None, stop=None, step=1):
    if stop is None:
        start, stop = 0, start

    result = []
    while start < stop:
        result.append(start)
        start += step
    return result


li = interval(1, 10, 2)
print li

print 'xx', range(10, -1)

print "================="


def getPrice(obj):
    if isinstance(obj, tuple):
        return obj[1]
    else:
        return 66


x = getPrice((1, 2))
print x

print 'abc'.count('b')
