def gcd(a, b):
    if b:
        return gcd(b, a % b)
    return a


def lcm(a, b): return a * b / gcd(a, b)


import sys

for line in sys.stdin.readlines():
    A, ans = map(int, line.strip().split())[1:], 1
    for a in A: ans = lcm(a, ans)
    print ans
