f = [10]


def dp(n):
    if len(f) > n:
        return f[n]
    if n == 1:
        f[-1] = 10
        return f[-1]
    f.append(dp(n - 1) + 2)
    return f[-1]


import sys

for line in sys.stdin.readlines():
    print dp(int(line.strip()))