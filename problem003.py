a = 600851475143

def prime(n):
	i = 2
	while(n%i != 0 and i < n):
		i += 1

	print(i)
	if(i < n):
		return prime(n/i)
	else:
		print("the highest prime factor is: %d" % n)

prime(600851475143)