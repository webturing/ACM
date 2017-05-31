while True:
    arr = raw_input().strip().split()
    if len(arr) == 1:
        break
    a = sorted(map(int, arr[1:]), key=abs)[::-1]
    print a
    print str(a)[1:-1].replace(',', '')
    
