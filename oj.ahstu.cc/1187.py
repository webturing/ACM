import sys

for line in sys.stdin.readlines():
    a1, b1, a2, b2 = map(int, line.strip().split())
    for i in xrange(1, 1 << 30):
        if i % a1 == b1 and i % a2 == b2:
            print i
            break
