import re
# from re import findall,search,S
f = file('b.txt')
data = f.read()

b = re.findall('(\d+)',data)
print b
i = 0
j = 0
out = open('a.txt', 'w')
for i in range(0,14):
	print b[i]+','+b[i+1]
	print i
    # j += 1
    # out.write(b[i])
    # if(j%2 == 0):
    #     out.write('\n')
    # else:
    #     out.write(',')
out.close()
