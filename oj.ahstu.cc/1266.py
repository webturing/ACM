import sys

for line in sys.stdin.readlines():
    a = map(int, line.strip().split())
    if max(a) == min(a) == -1:
        break
    find = False
    for i in a:
        if i <= 168:
            print "CRASH " + str(i)
            find = True
            break
    if not find:
        print 'NO CRASH'
