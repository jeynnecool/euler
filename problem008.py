chars = []

with open('1000digit.txt') as f:
	while True:
		c = f.read(1)

		if not c:
			print "End of file"
			break
		else:
			if(c != '\n'):
				n = int(c)
				chars.append(n)


def getNumber(l):
	num = 0
	for i in l:
		num = num * 10 + i
	return num

nums = []


index = 0
for i in chars:
	l = chars[index: index + 13]
	if len(l) == 13:
		if (0 not in l) and (1 not in l):
			nums.append(l)
	index = index + 1


final = []
for t in nums:
	print t
	r = 1
	for x in t:
		r = r * x
	final.append(r)

final2 = list(reversed(sorted(final)))

print final2[0]