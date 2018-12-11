# coding:utf-8
import threading
from time import sleep, ctime
from multiprocessing import Process

# loops = [4, 2]
#
#
# def loop1(noop, nsec):
#     print "loop1-1->", noop, "at", ctime()
#     sleep(nsec)
#     print "loop1-2->", noop, "at", ctime()
#
#
# def loop2(noop, nsec):
#     print "loop2-1->", noop, "at", ctime()
#     sleep(nsec)
#     print "loop2-2->", noop, "at", ctime()
#
#
# def main():
#     print "stat->", ctime()
#     threads = []
#     noop = range(len(loops))
#
#     for i in noop:
#         t = threading.Thread(target=loop1, args=(i, loops[i]))
#         threads.append(t)
#     for i in noop:
#         threads[i].start()
#
#     for i in noop:
#         threads[i].join()
#
#     print "end->", ctime()
#

# if __name__ == '__main__':
#     main()

"================================================"

# def f(name):
#     print 'hello', name
#
#
# if __name__ == '__main__':
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()

# "================================================"

import thread
from time import sleep
import time

loops = [4, 2]


def loop0():
    print 'start loop 0 at:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    sleep(4)
    print 'loop 0 done at:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


def loop1():
    print 'start loop 1 at:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    sleep(2)
    print 'loop 1 done at:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


def main():
    print 'start:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print 'all end:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


if __name__ == '__main__':
    main()
