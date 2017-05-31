import math


def prime(n):
    if n < 2: return False
    for c in xrange(2, int((math.sqrt(n) + 1))):
        if n % c == 0:
            return False
    return True


print str([x for x in xrange(1, 1 + int(raw_input())) if prime(x)])[1:-1].replace(',', '') + ' '
