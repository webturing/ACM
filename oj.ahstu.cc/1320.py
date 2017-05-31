import sys


def f(x):
    if x == 0: return 1
    return f(x - 1) + 2 * (x - 1)


for line in sys.stdin.readlines()[1:]:
    print f(int(line.strip()))
