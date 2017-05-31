import sys
import math

for line in sys.stdin.readlines()[1:]:
    radius = float(line)
    area = math.pi * radius * radius
    print '%.6f' % area
    
