v1, v2, t, s, l = map(int, raw_input().strip().split())
a, s1, s2, flag, tot, used = l / v2, 0, 0, 1, 0, 0
for i in xrange(a + 1):
    used = i
    if flag:
        s1 += v1
    elif tot < s:
        tot += 1
        flag = 0
    else:
        tot = 0
        flag = 1
    s2 += v2
    if flag and s1 >= s2 + t:
        flag = 0
        tot += 1
    if s1 >= l or s2 >= l:
        break
        # print s1,s2
if s1 == s2:
    print 'D'
elif s1 == l:
    print 'R'
else:
    print 'T'
print used + 1