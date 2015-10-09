monthsDict = {9 : 30, 
              4 : 30,
              6 : 30,
              11 : 30,
              1 : 31,
              3 : 31,
              5 : 31,
              7 : 31,
              8 : 31,
              10 : 31,
              12 : 31}
daysDict = {0 : "Sunday",
            1 : "Monday",
            2 : "Tuesday",
            3 : "Wednesday",
            4 : "Thursday",
            5 : "Friday",
            6 : "Saturday"}

#366 days going from Jan 1 1900 to Jan 1 1901, -1 for ending Dec 31 2000
days = 366
sundays = 0
for i in xrange(1901, 2001):
    for j in xrange(1, 13):
        if days % 7 == 0:
            sundays += 1
        if j == 2:
            if i % 400 == 0:
                days += 29
            elif i % 100 == 0:
                days += 28
            elif i % 4 == 0:
                days += 29
            else:
                days += 28
        else:
            days += monthsDict[j]
#            print days - 366
if days % 7 == 0:
    sundays -= 1
print sundays