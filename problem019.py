
def getLeapYears(startYear, endYear):
	leapYears = []
	for year in range(startYear, endYear+1):
		if year % 4 == 0:
			leapYears.append(year)
	return leapYears

LeapYears = getLeapYears(1900, 2000)

ThirtyDayMonth = [4, 6, 9, 11]

def getSundays():
	totalDay = 0
	for y in range(1901, 2001):
		if y in LeapYears:
			totalDay += 366
		else:
			totalDay += 365

	sundays = []
	for d in range(1, totalDay+1):
		if (d+366) % 7 == 0 and d > 31:
			sundays.append(d+366)
	return sundays

Sundays = getSundays()

FirstDayOfMonth1900 = [1, 32, 61, 92, 122, 153, 
183, 214, 245, 275, 306, 336]

def getFirstDayOfMonth(year):
	days = []
	normdiff = 0
	leapdiff = 0
	for y in range (1900, year):
		if y in LeapYears:
			leapdiff += 1
		else:
			normdiff += 1

	totalDiff = normdiff * 365 + leapdiff * 366
	for d in FirstDayOfMonth1900:
		days.append(d + totalDiff)

	return days

FirstDays = []
for y in range(1901, 2001):
	FirstDays = FirstDays + getFirstDayOfMonth(y)


TotalFirstDaySunday = []
for d in FirstDays:
	if d in Sundays:
		TotalFirstDaySunday.append(d)

print TotalFirstDaySunday
print len(TotalFirstDaySunday)