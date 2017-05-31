import math

while True:
    a, b, c = map(float, raw_input().strip().split())
    s = (a + b + c) / 2
    S = math.sqrt(s * (s - a) * (s - b) * (s - c))
    r1, r2 = 2 * S / (a + b + c), a * b * c / (4 * S)
    print '%.3f %.3f' % (math.pi * r1 ** 2, math.pi * r2 ** 2)
