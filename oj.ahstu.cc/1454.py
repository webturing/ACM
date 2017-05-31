import re

text = re.compile(r'\W+').split(raw_input().strip().lower())
for case in xrange(int(raw_input())):
    key = raw_input().lower()
    print len([x for x in text if x == key])
