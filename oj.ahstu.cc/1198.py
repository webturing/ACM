import sys


def foo(s):
    tot = 0
    for i in xrange(len(s)):
        for j in xrange(i + 1, len(s)):
            if s[i] > s[j]:
                tot += 1
    return tot


dnas = [x.strip() for x in sys.stdin.readlines()[1:]]
dnas = sorted(dnas, key=lambda d: foo(d))
for dna in dnas:
    print dna
