import sys

for line in sys.stdin.readlines():
    print "%X" % (sum(map(lambda x: int(x, 16), line.strip().split())))