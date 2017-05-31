import sys
import string

freq = {}
for i in xrange(26):
    freq[chr(ord('a') + i)] = 0
# print freq
for line in sys.stdin.readlines():
    for char in line.strip().lower():
        if char in string.letters:
            freq[char.lower()] += 1
for char in string.lowercase:
    print '%s %d' % (char, freq[char])