"""
関数
calendar.isleap(year)
戻り値
指定したyearがうるう年ならばTrue,それ以外はFalse
"""

import calendar
from datetime import datetime

now_dt = datetime.now()
res = calendar.isleap(now_dt.year)
print(res)
