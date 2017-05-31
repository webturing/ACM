import sys

for line in sys.stdin.readlines()[1:]:
    a, b, c = map(int, line.strip().split())
    d = a + b - c
    if d < 0:
        print 'Impossible'
    else:
        print d
