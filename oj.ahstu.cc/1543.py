import sys

for data in sys.stdin.readlines()[1::2]:
    arr0 = map(int, data.strip().split())
    arr1 = sorted(set(arr0))
    for num in arr0:
        print arr1.index(num) + 1,
    print