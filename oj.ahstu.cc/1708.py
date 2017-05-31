L, M = map(int, raw_input().strip().split())
T = [1] * (L + 1)
for cas in xrange(M):
    start, end = map(int, raw_input().strip().split())
    for i in xrange(start, end + 1):
        T[i] = 0
print sum(T)