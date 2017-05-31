import sys

for line in sys.stdin.readlines()[1:]:
    s = sorted(line.strip())
    print '%s %s %s' % (s[0], s[1], s[2])
