import sys

n, A, tot = int(sys.stdin.readline().strip()), [], 0
for i in xrange(n): A.append(map(int, sys.stdin.readline().strip().split()))
for i in xrange(n):
    for j in xrange(n):
        if i + j == n - 1 or i == j: tot += A[i][j]
print tot

