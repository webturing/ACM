import sys

for line in sys.stdin.readlines():
    n = int(line.strip())
    print n * (n + 1) / 2