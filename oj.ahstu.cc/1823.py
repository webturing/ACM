import sys

for line in sys.stdin.readlines():
    time, wage = map(float, line.strip().split())
    total = 0
    if time < 40:
        total = time * wage
    elif time < 50:
        total = 40 * wage + (time - 40) * wage * 1.5
    else:
        total = 40 * wage + 10 * wage * 1.5 + (time - 50) * wage * 2
    print '%.2f' % total
