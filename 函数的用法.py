# coding:utf-8


def cou(a, b):
    i = 0
    c = 0
    while i < len(a):
        if b in a[i]:
            c += 1
        i += 1
    print a, "\n", c


a = "hello world"
b = "l"
cou(a, b)

st = "cheng zheng hao shuai eng"


def countstr(s, sub):
    i = 0
    j = 0
    while i <= len(s) - len(sub):
        if s[i:i + len(sub)] == sub:
            j += 1
        i += 1
    # else:
    # 	print -1

    print j


countstr(st, "eng")
