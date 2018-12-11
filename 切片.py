s = "abcdefghijkjkjklmnabcdefghijklmnabcdefghijklmnjk"
sub = "jk"

i = 0
while i < len(s) - len(sub) + 1:
    if s[i:i + len(sub)] == sub:
        s = s[:i] + s[i + len(sub):]
        i -= 1
    i += 1
print s[:i], s[i + len(sub):]

# s = list(set(s))
# print s
