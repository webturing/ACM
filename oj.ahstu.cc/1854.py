'''
BUGS
'''
import math


def f(x): return math.sqrt(x ** 3)


N = 10
while True:
    a, b = map(float, raw_input().strip().split())
    dx = (b - a) / N
    L = 0
    for i in xrange(1, N + 1):
        dy = f(a + i * dx) - f(a + (i - 1) * dx)
        L += math.sqrt(dx ** 2 + dy ** 2)
    print '%.3f' % L
