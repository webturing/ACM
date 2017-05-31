import math


def prime(n):
    if n == 2: return True
    if n <= 1 or n % 2 == 0: return False
    end = int(1 + math.sqrt(n))
    for c in xrange(3, end, 2):
        if n % c == 0: return False
    return True


MX = int(raw_input()) + 1
dp = [0] * (MX + 1)
for i in xrange(1, (MX + 1)):
    dp[i] = (dp[i - 1] if not prime(i) else dp[i - 1] + i)
print dp[-1]