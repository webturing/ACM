import sys

for line in sys.stdin.readlines():
    n, m = map(int, line.strip().split())
    print '%.5f' % sum([1.0 / i ** 2 for i in xrange(n, m + 1)])
