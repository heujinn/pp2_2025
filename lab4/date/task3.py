import datetime

date_now = datetime.datetime.now()
date_now_womc = date_now.replace(microsecond=0)
print(date_now_womc)