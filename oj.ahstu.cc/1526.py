y, m = map(int, raw_input().strip().split())
d = 0
if m < 1 or m > 12:
    d = -1
elif m in [1, 3, 5, 7, 8, 10, 12]:
    d = 31
elif m in [4, 6, 9, 11]:
    d = 30
elif y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    d = 29
else:
    d = 28
if d > 0:
    print d
else:
    print 'Are you kidding~'
