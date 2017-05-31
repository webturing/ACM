def ok(s):
    try:
        d = int(s)
    except:
        return 0
    return 1000 >= d >= 1


while True:
    data = raw_input().strip().split()
    a, b = data[0], ''.join(data[1:])
    if ok(a) and ok(b):
        print '%d + %d = %d' % (int(a), int(b), int(a) + int(b))
    else:
        print '%s + %s = ?' % ((a if ok(a) else '?'), (b if ok(b) else '?'))
