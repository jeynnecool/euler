import os
import math

def ReadText():
	with open('p022_names.txt') as f:
		lines = f.readlines()
		return lines[0]

txt = ReadText()
lines = txt.split(',')

names = []
for l in lines:
	l = l.replace('"', '')
	names.append(l)

#print names

'''
orig = []
for i in range(0, len(names)):
	orig.append(i)

# def SortNames():
# 	for n in names:
# 		print n[0]

characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
'V', 'W', 'X', 'Y', 'Z']

def getCharIndex(c):
	return characters.index(c) + 1

powers = []
for n in names:
	power = []
	i = 0
	for c in n:
		power += getCharIndex(c) * (1 / (math.pow(10, i)))
		i += 1
	powers.append(power)

print powers
'''

names.sort()
print names

characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
'V', 'W', 'X', 'Y', 'Z']

scores = []

i = 1
for n in names:
	worth = 0
	for c in n:
		charIndex = characters.index(c) + 1
		worth += charIndex
	score = worth * i
	scores.append(score)
	i += 1

print scores

print sum(scores)