def Factorial(n):
	if n == 1:
		return 1
	else:
		return Factorial(n-1) * n

print Factorial(100)

s = str(Factorial(100))

total = 0
for cha in s:
	i = int(cha)
	total += i

print total