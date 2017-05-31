import sys

for line in sys.stdin.readlines()[:-1]:
    a, b = map(int, line.strip().split())
    print sum(xrange(a, b + 1))