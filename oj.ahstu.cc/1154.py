import sys

for line in sys.stdin.readlines():
    print ''.join(map(lambda char: '0' if char == '1'else '1', line.strip()))