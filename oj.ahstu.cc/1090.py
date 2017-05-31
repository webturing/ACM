import math


def prime(n):
    if n < 0:
        n = -n
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    start, end = 3, int(math.sqrt(n))
    for c in xrange(start, end + 1, 2):
        if n % c == 0:
            return False
    return True


number = int(raw_input())
total = 0
right = number / 2 if number % 4 != 0 else number / 2 - 1
for p in xrange(3, right + 1, 2):
    if prime(p) and prime(number - p):
        total += 1
print total
