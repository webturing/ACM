import sys
import string

for line in sys.stdin.readlines():
    word = []
    for char in line.strip():
        if char in string.letters:
            word.append(char)
        else:
            sys.stdout.write(''.join(word)[::-1])
            sys.stdout.write(char)
            word = []
    print
