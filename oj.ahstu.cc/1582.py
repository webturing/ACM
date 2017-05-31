import collections

n, a, b = int(raw_input()), collections.deque(map(int, raw_input().strip().split())), []
while a:
    b.append(a.popleft())
    if not a: break
    a.append(a.popleft())
print str(b)[1:-1].replace(',', '') + ' '