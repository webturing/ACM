a, n = map(int, raw_input().strip().split())
f = [a]
while len(f) < n: f.append(f[-1] * 10 + a)
print sum(f)
