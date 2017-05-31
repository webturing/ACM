cube = [x ** 3 for x in xrange(2048)]
import sys

for line in sys.stdin.readlines():
    if abs(int(line.strip())) in cube:
        print 'YES'
    else:
        print 'NO'
