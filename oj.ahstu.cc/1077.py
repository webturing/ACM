import sys


def cnr(n, r):
    return 1 if r == 0 or n == r else cnr(n - 1, r - 1) + cnr(n - 1, r)


def yh(n):
    for i in xrange(n - 1, -1, -1):
        sys.stdout.write(' ' * (n - i - 1))
        for j in xrange(0, i + 1):
            sys.stdout.write(str(cnr(i, j)) + ' ')
        sys.stdout.write('\n')
    sys.stdout.write('\n')


for line in sys.stdin.readlines():
    yh(int(line.strip()))
