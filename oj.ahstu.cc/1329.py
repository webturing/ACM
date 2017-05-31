import sys

while True:
    n, h = map(int, sys.stdin.readline().strip().split())
    A = map(int, sys.stdin.readline().strip().split())
    print sum([1 if x <= h else 2 for x in A])
