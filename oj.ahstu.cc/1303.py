a, b = map(int, raw_input().strip().split())
print (a / 10 + b / 10) % 10 * 10 + (a % 10 + b % 10) % 10