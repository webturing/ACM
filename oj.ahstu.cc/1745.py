n = int(raw_input())
a = map(int, raw_input().strip().split())
for i in xrange(0, n):
    k = i
    for j in xrange(i + 1, n):
        if a[j] < a[k]:
            k = j
    a[i], a[k] = a[k], a[i]
    print 'swap(a[%d], a[%d]):' % (i, k) + str(a).replace(',', '')[1:-1]