import calendar
from datetime import datetime

now_dt = datetime.now()
res = calendar.isleap(now_dt.year)
print(res)
