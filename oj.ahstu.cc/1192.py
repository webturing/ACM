while True:
    raw_input()
    A = raw_input().strip().split()
    gMax, tMax, cur = 0, 0, A[0]
    for a in A:
        if tMax > gMax:
            gMax = tMax
        if a == cur:
            tMax += 1
        else:
            cur = a
            tMax = 1
    print gMax
