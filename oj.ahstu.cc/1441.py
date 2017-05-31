import re

while True:
    key = raw_input().lower()
    text = re.compile(r'\W+').split(raw_input().strip().lower())
    print len([x for x in text if x == key])
