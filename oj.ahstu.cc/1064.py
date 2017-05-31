import sys
import math

for area in [4.0 / 3 * math.pi * r ** 3 for r in map(float, sys.stdin.readlines())]:
    print '%.3f' % area