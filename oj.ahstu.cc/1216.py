m, B = int(raw_input()), [100, 50, 20, 10, 5, 2, 1]
for b in B:
    while m >= b:
        print b
        m -= b