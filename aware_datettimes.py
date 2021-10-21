import datetime
import pytz


dt_utc_plus1 = datetime.datetime.now()  #
dt_eastern = dt_utc_plus1.astimezone(pytz.timezone('US/Eastern'))

print(dt_utc_plus1)
print(dt_eastern)

print(dt_eastern.isoformat())  # iso format, other formats available
print(dt_eastern.strftime('%B %d, %Y'))  # special format, other formats available

dt_string = 'June 25, 2020'

dt = datetime.datetime.strptime(dt_string, '%B %d, %Y')  # Convert string to datetime format

# strftime - datetime to string
# strptime - string to datetime

print(dt)