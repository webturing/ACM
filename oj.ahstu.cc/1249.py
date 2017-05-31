import sys

M = 1000


def mpow(a, b):
    if a == 1 or b == 0:
        return 1
    if b == 1 or a == 0:
        return a
    if b % 2 == 0:
        return mpow(a * a % M, b >> 1)
    return (mpow(a * a % M, b >> 1) * a) % M


for line in sys.stdin.readlines()[:-1]:
    a, b = map(int, line.strip().split())
    print mpow(a, b)