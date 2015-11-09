import math

def getSum(n):
	return n*(n+1)/2

def getFactorsCount(n):
	if n == 1:
		return 1
	else:
		factors = []
		root = int(math.sqrt(n)) + 1
		for i in range(1, root):
			if n % i == 0:
				factors.append(i)
				if (n/i) != i:
					factors.append(n / i)
		return len(factors)

l = 1
start = 1
while l < 500:
	num = getSum(start)
	l = getFactorsCount(num)
	if l >= 500:
		print num
	start += 1
