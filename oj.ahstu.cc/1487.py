while True:
    n = int(raw_input().strip())
    data = sorted(map(float, raw_input().strip().split()))
    if n % 2:
        print '%.2f' % data[n / 2]
    else:
        print '%.2f' % ((data[n / 2 - 1] + data[n / 2]) / 2.0)
