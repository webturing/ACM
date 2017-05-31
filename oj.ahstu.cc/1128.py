import math


def prime(n):
    if n < 2:
        return 'N'
    for c in xrange(2, int((math.sqrt(n) + 1))):
        if n % c == 0:
            return 'Y'
    return 'N'


import sys

for line in sys.stdin.readlines():
    print (prime(int(line)))