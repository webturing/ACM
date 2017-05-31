n = int(raw_input())
arr = map(int, raw_input().strip().split())
ans = sorted(arr, reverse=True)[0:10]
print str(ans)[1:-1].replace(',', '')
