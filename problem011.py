import sys

matrix = [[0 for x in xrange(20)] for x in xrange(20)]
bigNumb = 1

i = 0
with open('20x20digits.txt') as f:
	while True:
		c = f.readline()
		
		if not c:
			print "End of file"
			break
		else:
			s = str(c).replace('\n', '')
			nums = s.split(' ')
			row = []
			for s in nums:
				num = int(s)
				row.append(num)
			matrix[i] = row
			i = i + 1

for i in range(0, 20):
	try:
		for j in range(0, 17):
			total = 1
			for x in range(j, j+4):
				total = total * matrix[i][x]
			if total > bigNumb:
				bigNumb = total
	except:
		print sys.exc_info[0]
		raise

for j in range(0, 20):
	try:
		for i in range(0, 17):
			total = 1
			for x in range(i, i+4):
				total = total * matrix[x][j]
			if total > bigNumb:
				bigNumb = total
	except:
		print sys.exc_info[0]
		raise


for i in range(0, 17,):
	try:
		for j in range(0, 17):
			total = 1
			for t in range(0, 4):
				total = total * matrix[i+t][j+t]
			if total > bigNumb:
				bigNumb = total
	except:
		print sys.exc_info[0]
		raise

for i in range(19, 3, -1):
	try:
		for j in range(0, 17):
			total = 1
			for t in range(0, 4):
				total = total * matrix[i-t][j+t]
			if total > bigNumb:
				bigNumb = total
	except:
		print sys.exc_info[0]
		raise

print bigNumb