def f(n):
    if n == 1: return 'A'
    return f(n - 1) + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[n - 1] + f(n - 1)


import sys

for line in sys.stdin.readlines(): print f(int(line.strip()))
