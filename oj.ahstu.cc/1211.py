import sys

for n in [int(line.strip()) for line in sys.stdin.readlines()[1:]]:
    print '0' * (32 - len(str(bin(n))[2:])) + str(bin(n)[2:])