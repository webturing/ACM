for case in xrange(int(raw_input())):
    data = map(int, raw_input().strip().split())
    n = data[0]
    data = sorted(data[1:])
    dif = [data[i] - data[i + 1] for i in xrange(n - 1)]
    print 'yes' if min(dif) == max(dif) else 'no'
