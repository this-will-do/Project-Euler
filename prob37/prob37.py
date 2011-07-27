
def is_prime(num,list):
	import math
	if num == 1: return False
	test = math.ceil(math.sqrt(num))
	for c in list:
		if not num % c:
			return False
		if c >= test: 
			list.append(num)
			return True

primelist = [2,3,5,7]

def trunc_left(num,list):
	test = str(num)
	index = 1
	while index < len(test):
		 if int(test[index:]) not in list:
			return False
		 index += 1
	return True

def trunc_right(num,list):
	test = str(num)
	index = len(test)-1
	while index > 0:
		if int(test[:index]) not in list:
			return False
		index -= 1
	return True

i = 11
count = 0
res = []
while count < 13 and i < 100000000:
	if is_prime(i,primelist) and trunc_left(i,primelist) and trunc_right(i,primelist):
		count += 1
		res.append(i)
		print i

	i += 2			
	
			
print res
		
	
