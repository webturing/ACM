import sys
import re

for line in sys.stdin.readlines():
    a, b, c, d = line.strip().split('.')
    if re.match('^\\d+$', a + b + c + d):
        ip = map(int, [a, b, c, d])
        if max(ip) <= 255 and min(ip) >= 0:
            print 'Y'
        else:
            print 'N'
    else:
        print 'N'
