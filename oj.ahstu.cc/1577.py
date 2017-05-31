import sys

for line in sys.stdin.readlines():
    a, b, c = map(int, line.strip().split())
    if a == 0:
        if b == 0:
            if c == 0:
                print 'Abnormal'
            else:
                print 0
        else:
            print 1
    else:
        delta = b * b - 4 * a * c
        if delta > 0:
            print 2
        elif delta < 0:
            print 0
        else:
            print 1