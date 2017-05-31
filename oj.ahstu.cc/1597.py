class Item:
    def __init__(self, start, end):
        self.start, self.end = start, end


items = []
for case in xrange(int(raw_input())):
    start, end = map(int, raw_input().strip().split())
    items.append(Item(start, end))

tot = 0
while items:
    items = sorted(items, key=lambda t: t.end)
    start = 0
    tot += 1
    selected = []
    for item in items:
        if item.start >= start:
            start = item.end
            selected.append(item)
    for item in selected: items.remove(item)

print tot
