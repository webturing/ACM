while True:
    raw_input()
    data = map(int, raw_input().strip().split())
    key = int(raw_input())
    print len([x for x in data if x < key])