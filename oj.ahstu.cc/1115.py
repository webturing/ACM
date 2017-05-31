f = {}
for i in xrange(10):
    f[i] = 0
for p in xrange(1, int(raw_input()) + 1):
    for char in str(p):
        f[int(char)] += 1
for v in f.values():
    print v