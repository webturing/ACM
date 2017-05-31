A = [1]
for i in xrange(2, 26): A.append(A[-1] * i % 1000000)
n = int(raw_input())
if n > 25: n = 25
print sum(A[:n]) % 1000000
