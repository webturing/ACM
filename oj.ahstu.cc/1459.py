import sys

for line in sys.stdin.readlines():
    n, m = map(int, line.strip().split())
    # print 'm=',m,"n=",n
    for h in xrange(0, n + 1):
        if 4 * h + 2 * (n - h) == m:
            print h, n - h
            break