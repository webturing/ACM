import math

m = int(raw_input())
n = int(math.log(m, 2.0))
left, right = 2 ** n, 2 ** (n + 1)
# print left, m, right
# print m - left
print left if m - left <= right - m  else right
