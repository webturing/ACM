for case in xrange(int(raw_input())):
    num, inc, dec = map(int, raw_input().strip().split())
    s = '9' * inc + str(num)
    for i in xrange(dec):
        pos = -1
        for i in xrange(len(s) - 1):
            if ord(s[i]) < ord(s[i + 1]):
                pos = i
                break
        if pos >= 0:
            s = s[0:pos] + s[pos + 1:]
        else:
            s = s[0:-1]
    print int(s)