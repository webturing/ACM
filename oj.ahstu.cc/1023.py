import sys

for line in sys.stdin.readlines():
    A = map(int, line.strip().split())
    print max(A[:A.index(-1)])