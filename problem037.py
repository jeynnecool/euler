import math

limit = 1000000
primes = [2,3,5]
sieve = [0 for x in xrange(limit)]

for i in xrange(limit):
	sieve[i] = 1
sieve[0] = 0
sieve[1] = 0

def isPrime(n):
	root = int(math.sqrt(n)) + 1
	for i in xrange(2, root):
		if sieve[i] is True and n % i == 0:
			return False
	return True

for i in xrange(2, limit):
	if sieve[i]:
		if isPrime(i):
			for j in range(i+i, limit, i):
				sieve[j] = False

for i in xrange(6, limit):
	if sieve[i]:
		primes.append(i)

print primes

total = 0

for n in primes:
	if n > 10:
		isTrunctablePrime = True
		for l in xrange(1, len(str(n))+1):
			truncLeft = int(str(n)[:l])
			if truncLeft not in primes:
				isTrunctablePrime = False
				break
		for l in xrange(len(str(n))-1, -1, -1):
			truncRight = int(str(n)[l:])
			if truncRight not in primes:
				isTrunctablePrime = False
				break
		if isTrunctablePrime:
			total += n
			print n

print total