# -*- coding: utf-8 -*-
import pickle
import codecs

# f = file('a.txt')   #文件管理类的
# data = f.readline(2)  # readline readlines
# print data
# data = f.readline()  #第一行未读完的第二次接着读，到\n为止
# print data
# print data.strip("\n")  #strip("\n")可去掉空行

# data = 'dsgf fgsdg dfgsfdg sdgsdfgds \n sgfdsgdg'
# out = open('b.txt','w')
# out.write(data)
# out.close()


# f = file('c.txt')  #先读取要处理的文件
# lines = f.readlines()
# #print lines
# f.close()
#
# results = []
# for line in lines:
#     print line
#     data = line.split()
#     #print data
#
#     sum = 0
#     for score in data[1:]:
#         sum += int(score)
#     result = '%s \t: %d\n' % (data[0], sum)
#     #print result
#     results.append(result)
#
# #print results
# output = file('result.txt', 'w')
# output.writelines(results)
# output.close()
#


fw = open('a.txt', 'a')  # a每次写入不清空之前的；w会清空
# print fw.read(4)
fw.write("qwerty\nhdgdfg\n")
fw.close()

path = "a.txt"  # 需要打开的文件
config = codecs.open(path, 'r', 'utf-8')  # 如果有格式编码等问题可这样

config.close()

fw = open('A/cz', 'a')  # a每次写入不清空之前的，追加；w会清空
fw.write("qwerty\nhdgdfg\n")

fw.close()

cz = open('A/cz', 'r')  # 读文件
s = cz.read(3)
print s
cz.close()

f = open('a.txt', 'a')
x = {'1': 'cz', '2': "cz2"}
y = range(1, 10)
pickle.dump(y, f)
f.close()

f = open('aa.txt', 'w')

f.write("ml\ng5w\ne\n5b")

f.flush()

f.close()

f = file('a.txt')
# data = f.readline()
data = f.read()
# data = f.readlines()
print data
f.close()

data = raw_input('please input:')
out = open('output.txt', 'w')
out.write(data)
out.close()
