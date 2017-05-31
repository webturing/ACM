while True:
    a, b = map(int, raw_input().strip().split())
    if a == b == 0:
        break
    ans = [('%02d' % i) for i in xrange(100) if (a * 100 + i) % b == 0]
    print str(ans).replace(',', '').replace("'", '')[1:-1]
