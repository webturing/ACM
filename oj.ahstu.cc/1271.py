import math

r, h = map(float, raw_input().strip().split())
print 'Area=%.3f' % (math.pi * r * r * 2 + 2 * math.pi * r * h)
