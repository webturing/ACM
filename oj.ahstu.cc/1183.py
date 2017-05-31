def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)


def lcm(a, b): return a * b / gcd(a, b)


import sys

for line in sys.stdin.readlines()[1:]:
    a, b = map(int, line.strip().split())
    print gcd(a, b), lcm(a, b)
