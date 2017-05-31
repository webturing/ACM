import sys

missed, recieved, called = [0] * 10, [0] * 10, [0] * 10

for line in sys.stdin.readlines():
    idx, telephone = map(int, line.strip().split())
    if idx == 0: missed = [telephone] + missed[:-1]
    if idx == 1: recieved = [telephone] + recieved[:-1]
    if idx == 2: called = [telephone] + called[:-1]
for i in xrange(10):
    print missed[i], recieved[i], called[i]
