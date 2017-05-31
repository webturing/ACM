import sys


def gcd(a, b):
    return gcd(b, a % b) if b else a


tot = 0
dic = {}
for line in sys.stdin.readlines()[1:]:
    a, b = map(int, line.strip().split())
    g = gcd(a, b)
    a, b = a / g, b / g;
    if (a, b) in dic.keys():
        dic[(a, b)] += 1
    else:
        dic[(a, b)] = 1
print max(dic.values())