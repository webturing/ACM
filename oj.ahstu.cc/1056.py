n = int(raw_input())
a = map(int, raw_input().strip().split())
a = sorted(set(a))
n = len(a)
print n
print str(a)[1:-1].replace(',', '')
