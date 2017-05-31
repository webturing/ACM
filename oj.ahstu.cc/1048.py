import sys


def f(n):
    return sum([x for x in range(1, n) if n % x == 0])


for line in sys.stdin.readlines()[1:]:
    a, b = map(int, line.strip().split())
    if a == f(b) and b == f(a):
        print 'YES'
    else:
        print 'NO'