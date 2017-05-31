import sys

for line in sys.stdin.readlines():
    print sum(map(long, line.strip().split()))