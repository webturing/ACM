import sys

t = int(sys.stdin.readline())
for i in xrange(t):
    m, n = map(int, sys.stdin.readline().strip().split())
    A = []
    for r in xrange(m):
        A.append(map(int, sys.stdin.readline().strip().split()))
    find = False
    for r in xrange(1, m - 1):
        for c in xrange(1, n - 1):
            if A[r][c] > max(A[r - 1][c], A[r + 1][c], A[r][c - 1], A[r][c + 1]):
                print A[r][c], r + 1, c + 1
                find = True
    if not find:
        print None, m, n
