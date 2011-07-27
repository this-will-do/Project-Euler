def fibbonaci(a,b,sentinel,list):
	if a > sentinel: return
	
	list.append(a)
	fibbonaci(b,a+b,sentinel,list)
	return list

fuck = fibbonaci(1,2,4000000,[])
print fuck
res = 0
for c in fuck:
	if not c % 2:
		res += c

print res
	
	
