def RevNumber(n, rev):
	if (n == 0):
		return rev
	else:
		digit = n % 10
		partial = n // 10
		rev = rev * 10 + digit
		return RevNumber(partial, rev)


a = 999

while a >= 100:
	if a % 10 != 0:
		b = 999
		while b >= 100:
			if b % 10 != 0:
				c = a * b
				revC = RevNumber(c, 0)
				if revC == c:
					print str(a) + ',' + str(b) + ',' + str(c)
					break
			b = b - 1
	a = a - 1


