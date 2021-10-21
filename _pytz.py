import datetime
import pytz

# dt = datetime.datetime(2015, 4, 22, 12, 39, 45, tzinfo=pytz.UTC)  # timezone aware, with UTC offset

dt_now = datetime.datetime.now(tz=pytz.UTC)  # timezone aware, with UTC offset, preferred format

# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)  # timezone aware, with UTC offset

# print(dt)
# print(dt_now)
# print(dt_utcnow)

dt_mtn = dt_now.astimezone(pytz.timezone('US/Mountain'))  # Byta tidszon

print(dt_now)
print(dt_mtn)

for tz in pytz.all_timezones:  # Alla tidzoner i pytz module
    print(tz)