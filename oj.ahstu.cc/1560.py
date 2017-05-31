import sys

for line in sys.stdin.readlines():
    num = int(line.strip())
    ans = 0
    if num == 0:
        ans = 0
    elif num % 9 == 0:
        ans = 9
    else:
        ans = num % 9
    print ans
