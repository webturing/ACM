while True:
    n, m = map(int, raw_input().strip().split())
    if n == m == 0:
        break
    data = map(int, raw_input().strip().split())
    while len(data) < n:
        data = data + map(int, raw_input().strip().split())
    data.append(m)
    data = sorted(data)
    print str(data)[1:-1].replace(',', '')
