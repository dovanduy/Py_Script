# coding:utf-8
import thread
from time import sleep, ctime

def loop0(a,b):
	print 'start loop 0 at:', ctime()
	print "add->",a+b
	sleep(4)
	print "sub->",a-b
	print 'loop 0 done at:', ctime()

def loop1(a,b):
	print 'start loop 1 at:', ctime()
	print "chen->",a*b
	sleep(3)
	print "chu->",a/b
	print 'loop 1 done at:', ctime()

def loop2(a,b):
	print 'start loop 2 at:', ctime()
	print "a->",a
	sleep(2)
	print "b->",b
	print 'loop 2 done at:', ctime()

def main():
	print 'start:', ctime()
	"""start_new_thread()要求一定要有前两个参数。所以，就算我们想要运行的函数不要参数，我们也要传一个空的元组。"""
	thread.start_new_thread(loop0, (4,3))
	thread.start_new_thread(loop1, (8,6))
	thread.start_new_thread(loop2, (8,6))
	sleep(6)
	print 'all end:', ctime()
if __name__ == '__main__':
	main()

