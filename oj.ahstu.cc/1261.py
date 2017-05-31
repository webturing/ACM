import math

MAX = 1000000

prime = [True] * (MAX + 1)
sq = int(math.sqrt(MAX + 1))
prime[0] = prime[1] = False
for i in xrange(2, sq + 1):
    if prime[i]:
        for j in xrange(i * i, MAX + 1, i):
            prime[j] = False

n = int(raw_input())

tot = 1 if n >= 3 else 0
for i in xrange(3, n - 1, 2):
    if prime[i] and prime[i + 2]:
        tot += 1
print tot