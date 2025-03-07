from datetime import date, timedelta 

today = date.today()
d = today - timedelta(days = 5)

print(today.day - 5)
print(d)