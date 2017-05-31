flowers = [153, 370, 371, 407]
a, b = map(int, raw_input().strip().split())
if a < 153: a = 153
if b > 407: b = 407
for x in [x for x in flowers if b >= x >= a]:
    print x
