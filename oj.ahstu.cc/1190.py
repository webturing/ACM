while True:
    S = {}

    n, m = map(int, raw_input().strip().split())
    if n == m == 0:
        break


    def create(n):
        for i in xrange(1, n + 1):
            S[i] = {i}


    def join(a, b):
        if S[a] == S[b]:
            return
        cc = set(c for c in xrange(1, n + 1) if c in S[a] or c in S[b])
        S[a] = cc
        S[b] = cc
        for x in S[a]:
            for y in S[b]:
                if x != y:
                    join(x, y)


    create(n)

    for i in xrange(m):
        a, b = map(int, raw_input().strip().split())
        join(a, b)
    print len(set(''.join(str(x)) for x in S.values())) - 1
