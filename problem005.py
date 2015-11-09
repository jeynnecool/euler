import math

primeList = []
rest = []

def getFactors(n, l):
	f = l
	for i in range(1, n+1):
		if n % i == 0 and i == n:
			if i not in l:
				f.append(i)
		elif n % i == 0 and i != n:
			getFactors(i, f)
	return f


for i in range(2, 21):
	f = getFactors(i, [])
	if len(f) == 2:
		primeList.append(i)
	else:
		rest.append(i)

print primeList
print rest

total = 1
for i in primeList:
	total = total * i

print total

rest = []
for i in range(1, 21):
	if total % i != 0:
		rest.append(i)
print rest

total = total * 24
print total
rest = []
for i in range(1, 21):
	if total % i != 0:
		rest.append(i)
print rest



'''
def factors(n, l):
	f = l
	for i in range(1, n+1):
		if n % i == 0 and i == n:
			if i not in l:
				f.append(i)
		elif n % i == 0 and i != n:
			factors(i, f)
	return f

for b in list(reversed(numa)):
	numa.remove(range(b, 21))

numb = list(reversed(numa))

numc = []
waste = []

for b in numb:
	if b not in waste:
		numc.append(b)

	f = factors(b, [])
	f.remove(b)
	for c in f:
		if c not in waste:
			waste.append(c)


print numc
print waste


revNuma = list(reversed(numa))

result = 1

for i in revNuma:
	result = i * result
	revNuma.remove(i)
	for j i
'''