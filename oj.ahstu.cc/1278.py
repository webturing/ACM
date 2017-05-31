import math

n = float(raw_input())
r = n / 180 * math.pi
print '%.3f %.3f' % (math.sin(r), math.cos(r))
