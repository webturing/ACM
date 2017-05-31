while True:
    raw_data = raw_input().strip().split()
    data = sorted(map(float, raw_data[:-1]))[1:-1]
    name = raw_data[-1]
    print '%s %.2f' % (name, sum(data) / len(data))