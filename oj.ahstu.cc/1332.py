import sys

for line in sys.stdin.readlines():
    a, b = map(int, line.strip().split())
    s, a = 1, a % 1000
    for i in xrange(b):
        s = s * a % 1000
    print '0' * (3 - len(str(s))) + str(s)