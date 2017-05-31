B = [100, 50, 10, 5, 2, 1]


def f(n):
    tot = 0
    for b in B:
        tot += n / b
        n %= b
    return tot


import sys

for line in sys.stdin.readlines()[:-1]:
    data = map(int, line.strip().split())[1:]
    print sum(map(f, data))
