import sys

peaches = [1]
for i in xrange(1, 31):
    peaches.append(2 * (peaches[-1] + 1))
for line in sys.stdin.readlines():
    print peaches[int(line) - 1]