'''
Sieve of Atkin
https://en.wikipedia.org/wiki/Sieve_of_Atkin

Sieve of Eratosthenes
埃拉托斯特尼筛法
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

Prime number theorem
素数定理
https://en.wikipedia.org/wiki/Prime_number_theorem

http://www.csie.ntnu.edu.tw/~u91029/Prime.html

http://program-think.blogspot.com/2011/12/prime-algorithm-1.html
'''


import math

limit = 2000000
primes = [2, 3, 5]
sieve = []

for i in range(0, limit):
	sieve.append(True)

sieve[0] = False
sieve[1] = False 

def isPrime(n):
	root = int(math.sqrt(n)) + 1
	for i in range(2, root):
		if sieve[i] == True and n != i and n % i == 0:
			return False
	
	return True


for i in range(2, limit):
	if sieve[i]:
		if isPrime(i):	
			for j in range(i + i, limit, i):
				sieve[j] = False


total = 0
for i in range(0, limit):
	if sieve[i]:
		total += i


print total
