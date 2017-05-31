import sys

for line in sys.stdin.readlines():
    a, b, c = map(int, line.strip().split())
    find = False
    for n in xrange(10, 100 + 1):
        if n % 3 == a and n % 5 == b and n % 7 == c:
            print n
            find = True
            break
    if not find:
        print 'No answer'
