import sys

while True:
    line = sys.stdin.readline()
    if not line:
        break
    digits = []
    for i in xrange(int(line.strip())):
        i, j = map(int, sys.stdin.readline().strip().split())
        digits.append(i * 3 + j + 1);
    print ''.join(str(x) for x in digits)