import sys
import datetime

for line in sys.stdin.readlines():
    yy, mm, dd = map(int, line.strip().split())
    birthday = datetime.date(yy, mm, dd)
    thatday = birthday + datetime.timedelta(days=10000)
    print '%d-%d-%d' % (thatday.year, thatday.month, thatday.day)