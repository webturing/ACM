n = int(raw_input())
A = [] * n
for j in range(n):
    A.append(map(int, raw_input().strip().split()))
B = []
for i in xrange(n):
    if sum(x[i] for x in A) * 2 > n:
        B.append(i + 1)
print str(B)[1:-1].replace(',', '')
