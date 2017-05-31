def cnr(n, r):
    return 1 if n == r or r == 0 else cnr(n - 1, r - 1) + cnr(n - 1, r)


def yh(n):
    for i in xrange(n):
        for j in xrange(i):
            print cnr(i, j),
        print 1
    print


while True:
    n = int(raw_input())
    yh(n)
