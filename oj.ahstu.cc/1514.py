import sys

while True:
    line = sys.stdin.readline()
    if not line: break
    if line.strip() == '': continue
    data = line.strip().split()
    # print 'data:', data
    size, points = int(data[0]), data[1:]
    love, beloved = {}, {}
    for point in points:
        love[point] = beloved[point] = 0
    num = int(sys.stdin.readline())
    for i in xrange(num):
        begin, end = sys.stdin.readline().strip().split('@')
        begin, end = begin.strip(), end.strip()
        if begin == end: continue
        love[begin] += 1
        beloved[end] += 1
    for point in points:
        print point, beloved[point], love[point]
    print