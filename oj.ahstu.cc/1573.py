n = int(raw_input())
for cas in xrange(n):
    s = raw_input().strip()
    while len(s) > 1 and len(s) % 2 == 0 and s == s[::-1]:
        s = s[0:len(s) / 2]
    print len(s)

    
