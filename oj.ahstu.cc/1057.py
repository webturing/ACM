x, y = map(int, raw_input().strip().split())
print sum([x for x in xrange(x, y + 1) if x % 3 == 1 and x % 5 == 3])