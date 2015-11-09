i = 1
numbers = []

while i < 1000:
	if((i % 3) == 0 or (i % 5) == 0):
		numbers.append(i)	
	i = i + 1

total = sum(numbers)
print total