import sys

for line in sys.stdin.readlines()[1:]:
    print len([x for x in line if x.isdigit()])
