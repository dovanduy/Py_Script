# coding=utf-8
import thread
import time

loops = [4, 2]


def loop(nloop, nsec, lock):
    print 'start loop', nloop, 'at:', time.strftime('%H:%M:%S', time.localtime())
    time.sleep(nsec)
    print 'loop', nloop, 'done at:', time.strftime('%H:%M:%S', time.localtime())
    # 解锁
    lock.release()


def loop2(nloop, nsec, lock):
    print 'start loop2', nloop, 'at:', time.strftime('%H:%M:%S', time.localtime())
    time.sleep(nsec)
    print 'loop2', nloop, 'done at:', time.strftime('%H:%M:%S', time.localtime())
    # 解锁
    lock.release()


def main():
    print 'starting at:', time.strftime('%H:%M:%S', time.localtime())
    locks = []
    locks2 = []
    # 以 loops 数组创建列表，并赋值给 nloops
    nloops = range(len(loops))
    for i in nloops:
        # 创建一个锁的列表
        lock = thread.allocate_lock()
        lock2 = thread.allocate_lock()
        # 锁定
        lock.acquire()
        lock2.acquire()
        # 追加到 locks[]列表
        locks.append(lock)
        locks2.append(lock2)
        """
        为什么我们不在创建锁的循环里创建线程呢？有以下几个原因：(1) 我们想到实现线程的同步，所以要让“所
        有的马同时冲出栅栏”。(2) 获取锁要花一些时间，如果你的线程退出得“太快”，可能会导致还没有获得
        锁，线程就已经结束了的情况。
        """
    # 执行多线程
    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))
        thread.start_new_thread(loop2, (i, loops[i], locks2[i]))

    """
    在线程结束的时候，线程要自己去做解锁操作。最后一个循环只是坐在那一直等（达到暂停主线程的
    目的），直到两个锁都被解锁为止才继续运行。
    """
    for i in nloops:
        while locks[i].locked():
            pass
        while locks2[i].locked():
            pass
    print 'all end:', time.strftime('%H:%M:%S', time.localtime())


if __name__ == '__main__':
    main()
