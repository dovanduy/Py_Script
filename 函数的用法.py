# coding:utf-8


st = "cheng zheng hao shuai eng"


def countstr(s, sub):
    i = 0
    j = 0
    while i <= len(s) - len(sub):
        if s[i:i + len(sub)] == sub:
            j += 1
        i += 1
    print j


countstr(st, "eng")

# =============lambda===================
f = lambda x: x + "232"
print f('cz')

s = [1, 1, 1]
a = [2, 3, 2]

ss = map(lambda x, y: x + y, s, a)
print ss


# ==============lambda==================
def f(x):
    return lambda y: x + y


print f(1)(2)

# ===============filter=================
# 遍历序列中的每个元素，判断每个元素得到的bool值，如果为true则留下来   过滤
move_people = ['sb_a', 'sb_b', 'sb_c', 'd', 'e', 'f', 'g']
yes = filter(lambda n: n.startswith('sb'), move_people)
no = filter(lambda n: not n.startswith('sb'), move_people)
print '只有sb的元素=>>>', yes
print '没有sb的元素=>>>', no

# ===============reduce=================
# 处理一个序列，然后对序列进行操作
num_reduce = [1, 2, 3, 100]
print reduce(lambda x, y: x + y, num_reduce)

# ===============eval=================
# 有转换类型的作用， 还可计算表达式
mydict = "{'a':1,'b':2}"
newdict = eval(mydict)
print type(mydict), type(newdict)
print eval('1+3*8-5+9/3+1*8//2')

# ===============hash=================
# 能hash的都是不可变数据类型，不能hash的都是可变数据类型的
print hash(mydict)
# print hash(move_people)
