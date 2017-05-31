import sys


def ok(n):
    s = bin(n)[2:]
    s = '0' * (32 - len(s)) + s
    return s == s[::-1]


data = map(int, sys.stdin.readlines())
print len([x for x in data if ok(x)])
