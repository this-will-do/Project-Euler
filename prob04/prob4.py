def is_palindrome(input):
	str = ('%s' % input)
	front = 0
	back = len(str)-1
	ret = True
	while front < back:
		ret &= str[front] == str[back]
		if not ret: break
		front += 1
		back -= 1
	return ret

high = 0
a1 = 0
b1 = 0
b2 = 0

for a in xrange(999,1,-1):
	ret = a*a
	if is_palindrome(ret):
		high = ret
		a1 = a
		break;
for c in xrange(a1,999,1):
	for b in xrange(999,c,-1):
		ret = c*b
		if is_palindrome(ret):
			if ret > high:
				high = ret
				b1 = b
				b2 = c

print (high,b2,b1)
		

