import sys

for line in sys.stdin.readlines():
    a, b = line.strip().split()
    a, b = a[::-1], b[::-1]
    c = int(a) * int(b)
    print int(str(c)[::-1])
