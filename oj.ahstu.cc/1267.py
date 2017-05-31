import sys
import string

K = 'AWFCMSDPGBLX'
V = 'IIILoveeeeYu'
MAP = string.maketrans(K, V)
data = [line.strip() for line in sys.stdin.readlines()]
for each in data:
    if each == 'END': break
    print ''.join([char if char not in K else char.translate(MAP) for char in each])

