import re

for word in re.split('\\W+', raw_input().strip()):
    if word:
        print word
