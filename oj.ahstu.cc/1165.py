import sys

for line in sys.stdin.readlines():
    print bin(long(line.strip()))[2:]
