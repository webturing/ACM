for case in xrange(int(raw_input())):
    a, b, c = map(int, raw_input().strip().split())
    if a + b == c:
        print '%d+%d=%d' % (a, b, c)
    elif a - b == c:
        print '%d-%d=%d' % (a, b, c)
    elif b - a == c:
        print '%d-%d=%d' % (b, a, c)
    elif a * b == c:
        print '%d*%d=%d' % (a, b, c)
    elif a == b * c:
        print '%d/%d=%d' % (a, b, c)
    elif b == a * c:
        print '%d/%d=%d' % (b, a, c)
    else:
        print 'None'
