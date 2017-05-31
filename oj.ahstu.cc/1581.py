raw_input()
data = sorted(set(map(int, raw_input().strip().split())))
print len(data)
print str(data)[1:-1].replace(',', '')
