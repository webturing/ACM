import sys

for line in sys.stdin.readlines():
    a, b = line.strip().split()
    find = False
    for i in xrange(0, min(len(a), len(b))):
        if a[i] != b[i]:
            find = True
            print ord(a[i]) - ord(b[i])
            break
    if not find:
        print 0
