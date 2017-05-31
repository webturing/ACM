import sys


def foo(s):
    s = s.strip()
    pre, tot = s[0], 1
    for char in s[1:]:
        if char == pre:
            tot += 1
        else:
            sys.stdout.write('%d' % tot + pre)
            pre = char
            tot = 1
    print '%d' % tot + pre


map(foo, sys.stdin.readlines()[1:])