import sys

for line in sys.stdin.readlines()[1:]: print sum(map(int, line.strip().split()))