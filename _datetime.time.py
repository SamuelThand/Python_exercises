import datetime

# t = datetime.time  # naive
# t = datetime.time(9, 20, 45, 1000)  # h, m, s, ms

# print(t)
# print(t.hour)

dt = datetime.datetime(2020, 7, 29, 12, 13, 11, 111111)  #year, month, day, h, m, s, ms
print(dt)
print(dt.year)

# tdelta = datetime.timedelta(days=7)
tdelta = datetime.timedelta(hours=12)

print(dt + tdelta)
