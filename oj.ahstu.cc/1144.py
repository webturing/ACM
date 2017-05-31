import math


def prime(n):
    if n < 0: n = -n
    if n == 2: return True
    if n < 2 or n % 2 == 0:
        return False
    start, end = 3, int(math.sqrt(n))
    for c in xrange(3, end + 1, 2):
        if n % c == 0:
            return False
    return True


a, b = map(int, raw_input().strip().split())
for n in xrange(a, b + 1):
    if prime(n) and str(n) == str(n)[::-1]:
        print n