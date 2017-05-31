import sys
import math

for line in sys.stdin.readlines():
    x1, y1, x2, y2 = map(float, line.strip().split())
    print '%.3f' % math.hypot(x1 - x2, y1 - y2)
