for case in xrange(int(raw_input())):
    a, b = map(int, raw_input().strip().split())
    print (a + b) * (a + b + 1) / 2 + a + 1
