import datetime as dt
now = dt.datetime.now()
# Fetches current Date & Time
print(now)
year = now.year
print(year)
month = now.month
print(month)
weekday = now.weekday()
#computer starts counting from 0 i.e. Monday = 0 and so on.
print(weekday)
date_of_birth = dt.datetime(year=1998,month=5,day=5,hour=6,minute=5,second=00)
#00:00:00 is created by default if no input of hour, minute and second is given
print(date_of_birth)