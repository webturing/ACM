import math

a, b, c = map(float, raw_input().strip().split())
delta = b ** 2 - 4 * a * c
x1, x2 = (-b + math.sqrt(delta)) / (2 * a), (-b - math.sqrt(delta)) / (2 * a)
print '%.2f %.2f' % (x1, x2)