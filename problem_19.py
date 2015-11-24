from datetime import date

sundays = []
for y in range(1901, 2001):
    for m in range(1, 13):
        if date(y, m, 1).isoweekday() == 7:
            sundays.append((y, m))
print len(sundays)
