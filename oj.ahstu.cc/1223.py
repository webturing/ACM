import itertools

n = int(raw_input())
data = sorted(map(int, raw_input().strip().split()))
# print data
#print itertools.permutations(data, n)
for e in itertools.permutations(data, n):
    print ''.join(str(x) for x in e)
