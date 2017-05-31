import sys

for line in sys.stdin.readlines():
    print str(sorted(map(int, line.strip().split()))[::-1])[1:-1].replace(',', '')