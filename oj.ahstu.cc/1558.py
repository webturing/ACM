for case in xrange(int(raw_input())):
    m, n = map(int, raw_input().strip().split())
    print '%.2f' % (n * 100.0 / m) + '%'