import sys

for line in sys.stdin.readlines():
    number = int(line)
    total = sum(map(int, list(line.strip())))
    print 'yes' if number % total == 0 else 'no'