def f(n):
    if n == 0:
        return 3
    else:
        return (f(n - 1) - 1) * 2


for case in xrange(int(raw_input())):
    print f(int(raw_input()))
