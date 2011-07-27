prod = 1
for i in xrange(1,101):
	prod *= i

print sum(int(digit) for digit in str(prod))
