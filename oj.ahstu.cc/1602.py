primes = [2, 3, 5, 7]
for n in xrange(11, 10000, 2):
    flag = True
    for prime in primes:
        if prime * prime > n:
            break
        if n % prime == 0:
            flag = False
    if flag:
        primes.append(n)
a, b = map(int, raw_input().strip().split())

for n in xrange(a, b + 1):
    factors = []
    m = n
    while m > 1:
        for prime in primes:
            if prime > m:
                break;
            while m % prime == 0:
                factors.append(prime)
                m /= prime
    print str(n) + "=" + str(factors)[1:-1].replace(',', '*').replace(' ', '')
