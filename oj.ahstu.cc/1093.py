import sys

for line in sys.stdin.readlines():
    print max(map(int, line.strip().split()))