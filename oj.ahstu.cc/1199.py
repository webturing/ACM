import sys

for line in sys.stdin.readlines():
    a, b = map(int, line.strip().split())
    if a == b == 0:
        break
    print a + b