"""
月末の取得と判定
メソッド calendar.monthrange(year,month)
戻り値 月初曜日と月末日のタプルを返す
"""

import calendar

start_wd, end_day = calendar.monthrange(2020, 2)
print(start_wd, end_day)
