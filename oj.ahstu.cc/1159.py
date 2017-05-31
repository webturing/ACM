import sys

for line in sys.stdin.readlines():
    data = sorted(map(float, line.strip().split())[1:])[1:-1]
    print '%.2f' % (sum(data) / len(data))