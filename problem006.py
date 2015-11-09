import math

sum1 = 0
sum2 = 0

for i in range(1, 101):
	sum1 = sum1 + math.pow(i, 2)
	sum2 = sum2 + i

result = math.pow(sum2, 2) - sum1

print result