import sys

for line in sys.stdin.readlines():
    n, a = map(float, line.strip().split())
    n = n * 1000 / 3600
    t = n / -a
    print '%.3f' % (t * n / 2)