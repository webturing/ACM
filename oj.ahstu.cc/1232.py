import sys


def f(n):
    if n <= 2:
        return 1
    return f(n - 1) + f(n - 2)


for line in sys.stdin.readlines()[1:]:
    print f(int(line.strip()))
