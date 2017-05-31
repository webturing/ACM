import sys
import string

for line in sys.stdin.readlines():
    freq = {}
    for char in line.strip():
        if char not in string.letters: continue
        freq[char.lower()] = (1 if char.lower() not in freq.keys() else freq[char.lower()] + 1)
    ans = sorted(freq.keys(), key=lambda t: (-freq[t], t))
    print ''.join(ans)