import math

primes = [2,3,5,7,11,13]
last = 13

def isPrime(n):
	root = int(math.sqrt(n)) + 1
	result = True
	for i in primes:
		if i < root and n % i == 0:
			result = False

	return result


while len(primes) <= 10001:
	if isPrime(last):
		primes.append(last)

	last = last + 1

print primes
