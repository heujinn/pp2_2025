import datetime

date1 = input('Enter a 1st day (YYY-MM-DD): ')
date2 = input('Enter a 2nd day (YYY-MM-DD): ')

day1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
day2 = datetime.datetime.strptime(date2, "%Y-%m-%d")


diff = day1 - day2
diff_as_s = diff.total_seconds()
print(diff_as_s)