import math

U, D, H = map(float, raw_input().strip().split())
L = math.hypot((D - U) / 2, H)
area = (U + D) * H / 2
perimeter = (U + D + 2 * L)
print '%.2f\n%.2f' % (area, perimeter)