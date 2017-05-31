import sys

for line in sys.stdin.readlines():
    n = int(line.strip())
    for i in xrange(1, n + 1):
        if '7' in str(i) or i % 7 == 0:
            print i
            