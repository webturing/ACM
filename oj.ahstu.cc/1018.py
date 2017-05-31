a = int(raw_input())
A = [a * a - a + 1 + i for i in xrange(0, 2 * a, 2)]
print '%d*%d*%d=%d=' % (a, a, a, a ** 3) + str(A)[1:-1].replace(', ', '+')
