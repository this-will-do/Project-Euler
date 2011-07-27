def divisors(input):
	import math
	list = set()
	sentinel = int(math.ceil(math.sqrt(input)))
	for x in xrange(1,sentinel+1):
		if not input % x:
			list.add(x)
			list.add(input / x)
	return list

def divsum(input):
	sum = 0
	for i in divisors(input):
		if i < input:
			sum += i
	return sum

def check(a):
	da = divsum(a)
	return (not da == a and a == divsum(da))

#amicable = [False] * 10000
sum = 0
for i in xrange(0,10000):
	#amicable[i] = check(i+1)
	if check(i):
		sum += i

print sum



	


		
			
		
		
