for case in xrange(int(raw_input())):
    a, b, c, d = map(int, raw_input().strip().split())
    print abs(c * d - a * b)