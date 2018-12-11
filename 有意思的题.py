# -*- coding: utf-8 -*-
# @Time    : 2018/11/1 21:51
# @Author  : chengz
# @File    : 有意思的题.py
# @Software: PyCharm


def prime(k):
    """找质数因子"""
    v = []
    i = 2
    while i < k:
        if k % i == 0:
            k = k / i
            v.append(i)
            i -= 1
        i += 1
    v.append(k)
    return v


def pyramid(row, col):
    """打印金字塔"""
    for i in range(0, row):
        for j in range(1, col):
            mid = (col - 1) / 2 + 1
            if mid - i <= j <= i + mid:
                print '*',
            else:
                print ' ',
        print '\n',


def fibs(num):
    result = [1, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])

    return result


if __name__ == '__main__':
    print prime(100)
    pyramid(10, 20)
    print fibs(10)
