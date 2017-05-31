import sys

for line in sys.stdin.readlines():
    print 'yes no'.split()[int(line.strip()) % 2]