import sys

for line in sys.stdin.readlines()[1:]:
    n, m = map(int, line.strip().split())
    if m % 2 != 0 or m < 2 * n or m > 4 * n:
        print 'No answer'
    else:
        print '%d %d' % ((4 * n - m) / 2, (m - 2 * n) / 2)