import sys

for line in sys.stdin.readlines():
    n, m = map(int, line.strip().split())
    ans = 1
    for i in xrange(n, n - m, -1):
        ans *= i
    for i in xrange(m, 1, -1):
        ans /= i
    print ans