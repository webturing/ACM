money = int(raw_input())
total = 0
for one in xrange(1, money + 1):
    for two in xrange(1, money / 2 + 1):
        for five in xrange(1, money / 5 + 1):
            if one + 2 * two + 5 * five == money:
                total += 1
print total