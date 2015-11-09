def produceChain(n):
	if n % 2 == 0:
		return n / 2
	else:
		return 3 * n + 1


def getChain(n):
	depth = 1
	while n > 1:
		n = produceChain(n)
		depth = depth + 1
	return depth


term = 0
longest = 1

for num in range(837700, 1000000):
	t = getChain(num)
	if t > term:
		term = t
		longest = num


print term
print longest