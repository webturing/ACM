def ok(n):
    if n % sum(map(int, list(str(n)))) == 0:
        return 'Lucky Word'
    else:
        return 'No Answer'


import sys

for line in sys.stdin.readlines():
    print ok(int(line.strip()))