import sys

for line in sys.stdin.readlines()[1:]:
    n, m = map(int, line.strip().split())
    print sum([i % m for i in xrange(1, n + 1)])
