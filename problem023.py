import math

l = []
for x in range(0, 28124):
	l.append(0)

def getFactors(n):
	if n == 1:
		return [1]
	else:
		factors = []
		factors.append(1)
		root = int(math.sqrt(n)) + 1
		for i in range(2, root):
			if n % i == 0:
				factors.append(i)
				if (n/i) != i:
					factors.append(n/i)
		return factors

def getSum(factors):
	total = 0
	for f in factors:
		total += f
	return total

def isAbundent(n):
	f = getFactors(n)
	s = getSum(f)
	if s > n:
		return True
	else:
		return False

abunds = []

for i in range(1, 28124):
	if(isAbundent(i)):
		abunds.append(i)

for i in range(0, len(abunds)):
	for j in range(0, len(abunds)):
		total = abunds[i] + abunds[j]
		if(total <= 28123 and l[total] == 0):
			l[total] = 1


t = 0
for i in range(0, 28124):
	if(l[i] == 0):
		print i
		t += i

print t