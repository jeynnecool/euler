import math

def getProperDivisors(n):
	divisors = []
	if n == 1:
		divisors = []
	elif n == 2:
		divisors.append(1)
	else:
		root = int(n/2) + 1
		for i in range(1, root + 1):
			if n % i == 0:
				divisors.append(i)
	return divisors


def getAmicableNumber(x):
	divisors = getProperDivisors(x)
	total = 0
	for i in divisors:
		total += i
	divisors2 = getProperDivisors(total)
	total2 = 0
	for i in divisors2:
		total2 += i
	if total2 == x and total != x:
		return total2
	else:
		return 0

amicables = []

for x in range(2, 10001):
	if x not in amicables:
		ami = getAmicableNumber(x)
		if ami > 0:
			amicables.append(ami)

print sum(amicables)