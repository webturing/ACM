def fact(n):
    s = 1
    for i in xrange(2, n + 1):
        s *= i
    return s


print fact(1977)
