import sys

data = [line.strip() for line in sys.stdin.readlines()[1:]]
data = sorted(data, key=lambda t: (-int(t[6:14]), long(t)))
for d in data: print d
