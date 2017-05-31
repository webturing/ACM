def fact(n):
    if n < 2:
        return 1
    return fact(n - 1) * n


print sum(map(fact, xrange(1, int(raw_input()) + 1)))