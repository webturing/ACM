import math

m = int(math.sqrt(int(raw_input())))
x, y = m ** 2, (m + 1) ** 2
print (x if m - x < y - m else y)
