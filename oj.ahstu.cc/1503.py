import sys


def gcd(a, b):
    return gcd(b, a % b) if b else a


for line in sys.stdin.readlines():
    data = map(int, line.strip().split())
    tot = 0
    for i in xrange(1, data[0] + 1):
        for j in xrange(1, i):
            if gcd(data[i], data[j]) == 1:
                tot += 1
    print tot