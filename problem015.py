def innerLine(n):
	return (2 * n) * n - (2 * n)

def factorial(x):
	if x == 1:
		return 1
	else:
		return factorial(x-1) * x

def getLatticePath(n):
	print factorial(2*n) / factorial(n)**2

print getLatticePath(20)