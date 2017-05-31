rank = 'EEEEEEDCBAA'
import sys

for line in sys.stdin.readlines():
    score = int(line.strip())
    if score < 0 or score > 100:
        print 'Score is error!'
    else:
        print rank[score / 10]