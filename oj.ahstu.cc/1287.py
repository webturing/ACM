import sys


def foo(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return foo(n / 2) + 1
    else:
        return foo(3 * n + 1) + 1


for line in sys.stdin.readlines():
    for n in map(int, line.strip().split()):
        print foo(n)