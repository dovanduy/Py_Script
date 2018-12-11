# coding:utf-8
s = "cheng zheng shi ge hao xuesheng "
sub = raw_input("")
# print len(sub)
i = 0
while i < len(s) - len(sub) + 1:
    if s[i:i + len(sub)] == sub:
        print i
    i += 1

# 打印第一个出现的位置
if sub in s:
    print s.find(sub)
