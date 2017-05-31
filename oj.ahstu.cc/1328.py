import sys

for line in sys.stdin.readlines():
    line = line.strip()
    print line[0].upper() + line[1::].lower()