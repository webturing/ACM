import sys


def tom(n):
    return sum(map(int, list(n)))


for n in sys.stdin.readlines():
    print tom(n.strip())