# coding:utf-8
import time
from concurrent.futures import ThreadPoolExecutor

p = ThreadPoolExecutor(30)  # 创建1个程池中，容纳线程个数为30个；


def get_time(times):
    print time.time()
    return times


def main():
    for i in range(1, 10):
        print 'one=>>>', p.submit(get_time, i).done()
        print 'two=>>>', p.submit(get_time, i).done()
        print 'three=>>>', p.submit(get_time, i).result(10)


if __name__ == '__main__':
    main()
