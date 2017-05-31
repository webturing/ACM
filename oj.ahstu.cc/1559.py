import sys

for line in sys.stdin.readlines()[1:]:
    print ''.join([char for char in line if char in '0123456789'])