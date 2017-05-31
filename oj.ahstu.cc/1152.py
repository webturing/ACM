import math
# TODO
print sum(xrange(297, 329))
while True:
    M = int(raw_input())
    for c in xrange(1, int(math.sqrt(M * 2)) + 1):
        if M % c == 0:
            m, n = c, 2 * M / c
            a, b = (n + 1 - m) / 2, (m + n - 1) / 2
            a, b = sorted((a, b))
            if b > a > 0 and sum(xrange(a, b + 1)) == M:
                print a, b
