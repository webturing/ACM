import sys


def count(char):
    if '8' == char:
        return 2
    if char in '069':
        return 1
    return 0


for line in sys.stdin.readlines():
    print sum(map(count, line.strip()))