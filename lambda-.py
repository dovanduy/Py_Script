s = [1, 1, 1]
a = [2, 3, 2]
# f = lambda x: x + 10

ss = map(lambda x, y: x + y, s, a)
print ss


def f(x):
    return lambda y: x + y


print f(1)(2)
