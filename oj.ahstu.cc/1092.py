def foo(m):
    for i in xrange(1, 9):
        r = int(str(m)[::-1])
        m = r + m
        if str(m) == str(m)[::-1]:
            return i
    return 0


for case in xrange(int(raw_input())):
    print foo(int(raw_input()))
