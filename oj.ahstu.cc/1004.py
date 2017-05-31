import itertools

A = sorted(map(int, raw_input().strip().split()))
for j in xrange(3, -1, -1):
    for i in itertools.permutations(A[0:j] + A[j + 1:], 3):
        print str(i)[1:-1].replace(',', '') + ' '
