a = '0123456789ABCDEFGHIJKLMNOPRSTUVWXY'
b = '0123456789222333444555666777888999'
import string

lett = string.maketrans(a, b)


def standard(s):
    t = ""
    for char in s:
        if char in a:
            t += char.translate(lett)
    return t[0:3] + "-" + t[3:]


# print standard('TUT-GLOP')
dic = {}
for case in xrange(int(raw_input())):
    cur = standard(raw_input().strip())
    if cur in dic:
        dic[cur] += 1
    else:
        dic[cur] = 1
# print dic
if max(dic.values()) == 1:
    print 'No duplicate.'
else:
    for key in sorted(dic.keys()):
        if dic[key] > 1:
            print key, dic[key]