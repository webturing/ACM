import sys
import datetime

for line in sys.stdin.readlines():
    year, month, day = map(int, line.strip().split('/'))
    today = datetime.date(year, month, day)
    start = datetime.date(year, 1, 1)
    print (today - start).days + 1