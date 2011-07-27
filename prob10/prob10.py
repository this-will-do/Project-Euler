def prime():
	import math
	primelist = [2,3]
	num = 5
	sum = 5
	while num < 2000000:
		test = math.ceil(math.sqrt(num))
		for c in primelist:
			if not num % c:
				break
			if c >= test: 
				primelist.append(num)
				sum += num
				break
			
		num += 2

	return sum


print prime()

			
		
	
