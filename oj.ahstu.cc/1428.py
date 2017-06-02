for case in xrange(int(raw_input())):
    n = int(raw_input())
    data = sorted(set(map(int, raw_input().strip().split())))
    idx = int(raw_input())
    print data[-idx]
