count = 0
numbers = []

def fib(n):
	if(n == 0):
		return 1
	elif(n == 1):
		return 2
	else:
		return fib(n - 1) + fib(n - 2)

current = fib(count)

while(current <= 4000000):
	print current
	if((current % 2) == 0):
		print("add")
		numbers.append(current)
	count = count + 1
	current = fib(count)

print sum(numbers)