def isSorted(a):
    inc = sorted(a)
    dec = inc[::-1]
    return a == inc or a == dec


import sys

for line in sys.stdin.readlines():
    a = map(int, line.strip().split())
    print 'YES' if isSorted(a) else 'NO'