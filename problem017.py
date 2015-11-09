word1 = ['one', 'two', 'three', 'four', 'five', 
'six', 'seven', 'eight', 'nine']

word2 = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 
'sixteen', 'seventeen', 'eighteen', 'nineteen']

word3 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 
'seventy', 'eighty', 'ninety']

# chars = []

def getLen(w):
	return len(w.replace(' ', ''))

total1To9 = 0
for w in word1:
	total1To9 = total1To9 + len(w)

total10 = len('ten')

total11To19 = 0
for w in word2:
	total11To19 = total11To19 + len(w)

total20To99 = 0
for w in word3:
	total20To99 = total20To99 + len(w) * 10 + total1To9

total1To99 = total1To9 + total10 + total11To19 + total20To99

total100To199 = len('one') * 100 + len('hundred') * 100 + len('and') * 99 + total1To99

total100To999 = total1To9 * 100 + len('hundred') * 100 * 9 + len('and') * 99 * 9 + total1To99 * 9

total1000 = len('onethousand') 

final = total1To99 + total100To999 + total1000

print final