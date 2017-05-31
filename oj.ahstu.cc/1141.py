while True:
    n = int(raw_input())
    if n == 0:
        break
    data = set(int(x) for x in raw_input().strip().split())

    print len(data)
    print str(sorted(data))[1:-1].replace(',', '')
    print

