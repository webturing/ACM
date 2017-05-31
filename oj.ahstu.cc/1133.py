while True:
    p, q = map(float, raw_input().strip().split())
    find = False
    for n in xrange(200):
        for m in xrange(n):
            if p < 100. * m / n < q:
                find = True
                print n
                break
        if find:
            break