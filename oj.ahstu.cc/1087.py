import sys

for line in sys.stdin.readlines():
    print ''.join([x for x in line if not x.isspace()])
