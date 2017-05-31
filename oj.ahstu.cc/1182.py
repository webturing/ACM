import sys

for line in sys.stdin.readlines()[1:]:
    print ''.join([char.upper() if char.islower() else char.lower() for char in line.strip()])