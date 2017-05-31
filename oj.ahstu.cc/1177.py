def fact(n):
    s = 1
    for i in xrange(2, n + 1):
        s *= i
    return s


import sys

for line in sys.stdin.readlines():
    print fact(int(line.strip()))
