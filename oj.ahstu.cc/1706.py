words = raw_input().strip().split()
print sorted(words, key=lambda w: -len(w))[0]
