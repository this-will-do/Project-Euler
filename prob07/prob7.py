def prime(max):
	import math
	primelist = [2,3]
	count = 2
	num = 4
	while count < max:
		test = math.ceil(math.sqrt(num))
		for c in primelist:
			if not num % c:
				break
			if c >= test: 
				primelist.append(num)
				count += 1
				break
			
		num += 1

	return primelist


print prime(10001)

			
		
	
