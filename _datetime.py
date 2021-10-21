import datetime

#Naive dates, times don't have enough info to determine timezones etc.
#Aware dates, times do have info to determine things like this

# d = datetime.date(2020, 1, 22)
# print(d)
tday = datetime.date.today()
# print(tday)
# print(tday.day)
# print(tday.weekday())
# print(tday.year)
# print(tday.day)
# print(tday.isoweekday())  #Vecka börjar måndag
# print(tday.weekday())  #Vecka börjar söndag

tdelta = datetime.timedelta(days=7)

# print(tday + tdelta)
# print(tday - tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2022, 2, 20)

till_bday = bday - tday
# print(till_bday.days)
print(f'{till_bday.total_seconds():_}')

