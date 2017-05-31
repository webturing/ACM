year = int(raw_input().strip())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print 'yes'
else:
    print 'no'