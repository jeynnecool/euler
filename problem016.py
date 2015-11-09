import math

def getTotal(n):
	s = str(int(math.pow(2, n)))
	total = 0
	for c in s:
		total = total + int(c)
	return total


print getTotal(1000)
