import sys
import math


def ok(n):
    start, end = 2, int(math.sqrt(n))
    tot = 0
    for i in xrange(start, end + 1):
        if n % i == 0:
            tot += 2
    return tot == 2


for line in sys.stdin.readlines()[1:]:
    print 'Yes' if ok(int(line.strip())) else 'No'
