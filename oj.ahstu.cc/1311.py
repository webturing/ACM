def prime(n):
    if n == 1:
        return False
    for c in xrange(2, n):
        if n % c == 0:
            return False
    return True


a, b = map(int, raw_input().strip().split())
print len([x for x in range(a, b + 1) if prime(x)])
