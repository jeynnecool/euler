import math

nth = []

def totalPermutation(n):
	res = 1
	if n <= 1:
		res = 1
	else:
		res = totalPermutation(n-1) * n
	nth.append(res)
	return res

totalPermutation(10)

print nth

# def getPermutation(n):
# 	total = 1
# 	for i in range(n, 0, -1):
# 		total = total * i
# 	return total

remain = 1000000
# d = [0,1,2,3,4,5,6,7,8,9,10]
# r = 9

# for i in range(9, -1, -1):
# 	a = 1
# 	while remain > nth[i]:
# 		a = a + 1
# 		remain = remain - nth[i]
# 	print a
# 	r = r - 1

# print totalPermutation(9)

# remain = 1000000 - total
# n = 9
# while n > 0 and remain > 0:
# 	print n
# 	print remain
# 	n -= 1
# 	total = totalPermutation(n)
# 	remain = remain - total


remain = remain - totalPermutation(9) * 2
print remain
remain = remain - totalPermutation(8) * 6
print remain
remain = remain - totalPermutation(7) * 6
print remain
remain = remain - totalPermutation(6) * 2
print remain
remain = remain - totalPermutation(5) * 5
print remain
remain = remain - totalPermutation(4)
print remain
remain = remain - totalPermutation(3) * 2
print remain
remain = remain - totalPermutation(2) * 2
print remain


# total = 0
# for i in range(8, -1, -1):
# 	print i
# 	subTotal = nth[i]
# 	while total < 1000000:
# 		total += subTotal
# 		print total