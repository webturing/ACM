fib = [1, 1]
for i in xrange(40):
    fib.append(fib[-1] + fib[-2])
print str(fib[:int(raw_input())])[1:-1].replace(',', '') + ' '