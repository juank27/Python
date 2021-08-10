import datetime

my_time = datetime.datetime.now()
my_time2 = datetime.datetime.utcnow()
print(my_time)
print(my_time2)

my_day = datetime.date.today()
print(f'Year: {my_day.year}')
print(f'Month: {my_day.month}')
print(f'Day: {my_day.day}')
