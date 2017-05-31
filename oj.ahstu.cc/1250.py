import sys

for line in sys.stdin.readlines():
    n, p = map(int, line.strip().split())
    mn, mx = int('1' * n), int(str(p) * n)
    # print mn,mx
    for i in xrange(mn, mx + 1):
        if max(map(int, list(str(i)))) <= p and '0' not in str(i):
            print i