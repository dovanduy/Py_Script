# coding:utf-8
def foo(*x):
	s = 0
	for i in x:
		s += i
	return s


fo = foo(1, 2, 3, 4, 5)
print fo


def fuu(**x):
	s = 0
	for i in x.values():
		s += i

	return s


fu = fuu(a=1, b=2, c=3, d=4, e=5, f=6)
print fu

"============================================"
s = "cheng"
ls = enumerate(s)
for i in ls:
	print i,





