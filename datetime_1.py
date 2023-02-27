import datetime
tday = datetime.date.today()
# in here monday is 0 and sunday is 6 print(tday.weekday())
# in here monday is one and sunday is 7 print(tday.isoweekday())

#time deltas are the difference between two dates or times
tdelta =datetime.timedelta(days=7)
print(tday + tdelta)

#calculated 7 days after from now

print(tday - tdelta)

#calculated 7 days before from now

bday = datetime.date(2023, 8, 12)
print(bday - tday)

#calculates how many days left to my birthday