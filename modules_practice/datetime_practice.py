import datetime

print(datetime.datetime.now())
print(datetime.date.today())

christamas = datetime.date(2025, 12, 25)
print(christamas)

today = datetime.date.today()

days_until_christmas = (christamas - today)
print(days_until_christmas)

