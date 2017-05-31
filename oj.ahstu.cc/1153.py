def prime(n):
    if n < 2:
        return False
    for c in xrange(2, n):
        if n % c == 0:
            return False
    return True


primes = [x for x in range(100, 200) if prime(x)]
print len(primes)
print str(primes)[1:-1].replace(',', '')
