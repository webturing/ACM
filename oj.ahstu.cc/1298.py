while True:
    a, b, c = map(int, raw_input().strip().split())
    print ('%.' + str(c) + 'f') % (float(a) / b)