fib = [1, 1]
for case in xrange(int(raw_input().strip())):
    k = int(raw_input())
    while len(fib) < k:
        fib.append(fib[-1] + fib[-2])
    print fib[k - 1]
