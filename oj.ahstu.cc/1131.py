def fact(n):
    s = 1
    for i in xrange(2, n + 1): s *= i
    return s


def cnr(n, r):
    return fact(n) / fact(r) / fact(n - r)


import sys

for line in sys.stdin.readlines():
    n, r = map(int, line.strip().split())
    print cnr(n, r)