a, b, c = sorted(map(int, raw_input().strip().split()))
if a ** 2 + b ** 2 == c ** 2:
    print 'yes'
elif a + b > c:
    print 'no'
else:
    print 'not a triangle'
