n = int(raw_input())
while n > 1:
    if n % 2 == 0:
        m = n / 2
        print '%d/2=%d' % (n, m)
        n = m
    else:
        m = 3 * n + 1
        print '%d*3+1=%d' % (n, m)
        n = m

        
