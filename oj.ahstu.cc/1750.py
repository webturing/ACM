number, height = map(int, raw_input().strip().split())
apples = map(int, raw_input().strip().split())
reaches = [apple for apple in apples if apple <= height + 30]
print len(reaches)
