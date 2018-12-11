# coding:utf-8


class Per(object):

    @staticmethod
    def eat(a):
        print "this is eat method", a

    @classmethod
    def clsmain(cls):
        print "this is ===",cls.__name__

    def __init__(self, name="cheng", color="pink"):
        self.name = name
        self.color = color
        print "gou zao  han shu", name, " ", color

    def __del__(self):
        print "xi gou han shu", self.name

    def run(self):
        print "run method name:", self.name


ins1 = Per()
ins1.eat('66')

print "zzz:", ins1.name, ins1.color
ins2 = Per("cz2")
ins2.run()
ins2.eat('77')
print "yyy:", ins2.name, ins2.color
ins3 = Per("cz3", "blue")
ins3.run()
ins3.eat('88')
print "xxx:", ins3.name, ins3.color

del ins1, ins2, ins3

Per.eat('999')
Per.clsmain()