import sys

for line in sys.stdin.readlines():
    x, y = map(int, line.strip().split())
    A = xrange(x, y + 1)
    odd = [x ** 2 for x in A if x % 2 == 0]
    even = [x ** 3 for x in A if x % 2 == 1]
    print '%d %d' % tuple(map(sum, [odd, even]))