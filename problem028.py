import math

def problem28():
	total = 1
	for i in range(3, 1002, 2):
		t = i * i
		s = t * 4 - (i-1) * 6
		total += s
	return total


print problem28()