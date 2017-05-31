import sys

for line in sys.stdin.readlines()[1:]:
    AH, AM, AS, BH, BM, BS = map(int, line.strip().split())
    CH, CM, CS = AH + BH, AM + BM, AS + BS
    CM += CS / 60
    CS %= 60
    CH += CM / 60
    CM %= 60
    CH %= 24
    print '%d %d %d' % (CH, CM, CS)
