# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 18:14
# @Author  : chengz
# @File    : debug.py
# @Software: PyCharm

import time


def timer(fun):
    def warp():
        start_time = time.time()
        fun()
        stop_time = time.time()
        print "runner=>>>", stop_time - start_time

    return warp


@timer
def test():
    time.sleep(1)
    print "==over=="


# res = timer(test) # 相当于@timer
# res() # 执行的是warp()

test()