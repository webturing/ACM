def factorial(n):
    s = 1L
    for i in xrange(2, n + 1):
        s *= i
    return s


print factorial(int(raw_input()))