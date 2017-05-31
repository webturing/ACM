while True:
    n = int(raw_input())
    k = int(raw_input()) % 4
    A = {}
    for i in xrange(n):
        data = map(int, raw_input().strip().split())
        for j in xrange(n):
            A[(i, j)] = data[j]
    # print A
    for t in xrange(k):
        B = {}
        for i in xrange(n):
            for j in xrange(n):
                B[(n - 1 - j, i)] = A[(i, j)]
        A = B
    for i in xrange(n):
        for j in xrange(n):
            print A[(i, j)],
        print
