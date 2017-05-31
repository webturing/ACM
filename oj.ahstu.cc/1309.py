import math

a, b, c = map(float, raw_input().strip().split())
s = (a + b + c) / 2
a, b, c = sorted([a, b, c])
if a + b <= c:
    print 'Input error!'
else:
    print '%.2f' % (math.sqrt(s * (s - a) * (s - b) * (s - c)))