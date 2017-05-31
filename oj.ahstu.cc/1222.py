import sys

while True:
    case = int(sys.stdin.readline())
    flag = int(sys.stdin.readline())
    A = sorted(map(int, sys.stdin.readline().strip().split()))
    if flag: A = A[::-1]
    for a in A: print a
