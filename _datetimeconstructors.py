import datetime

dt_today = datetime.datetime.today()  # timezone None
dt_now = datetime.datetime.now()  # Optional to pass timezone
dt_utcnow = datetime.datetime.utcnow()  # current utc time, timezone None

print(dt_today)
print(dt_now)
print(dt_utcnow)
