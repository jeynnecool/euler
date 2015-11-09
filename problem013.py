rangedigits = []

with open('100x50digits.txt') as f:
	while True:
		c = f.readline()

		if not c:
			print "End of file"
			break
		else:
			d1 = int(c[:12])
			rangedigits.append(d1)

#print firstdigits

total = 0
for n in rangedigits:
	total = n + total

print str(total)[:10]