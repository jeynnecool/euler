lines = []
with open('p067_triangle.txt') as f:
	for line in f:
		if not line:
			break
		else:
			line = line.replace('\n', '')
			print line
			lines.append(line)



def getLine(i):
	after = []
	current = lines[len(lines) - i]
	for s in current.split(' '):
		n = int(s)
		after.append(n)
	return after


def getNewLine(numBottom, numSecondBottom):
	nums = []

	for i in range(0, len(numSecondBottom)):
		n = numSecondBottom[i]
		left = numBottom[i] + numSecondBottom[i]
		right = numBottom[i+1] + numSecondBottom[i]
		if left > right:
			nums.append(left)
		else:
			nums.append(right)

	return nums


line1 = []

for i in range(1, len(lines)):
	if i == 1:
		line1 = getLine(i)
	
	line2 = getLine(i+1)
	line1 = getNewLine(line1, line2)

	print line1
	print line2