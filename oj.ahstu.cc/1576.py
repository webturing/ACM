import sys

for line in sys.stdin.readlines():
    data = map(int, line.strip().split())[1:]
    data = sorted(data)
    print data[-1] - data[0]
    
