import sys

for line in sys.stdin.readlines():
    line = line.strip()
    maxChar = max(list(line))
    print line.replace(maxChar, maxChar + '(max)')