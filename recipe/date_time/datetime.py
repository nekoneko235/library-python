"""
日付や時間の型
型 役割
date      日付を扱う
datetime  日時を扱う
time      時間を扱う
timedelta 日付、時間の計算を扱う

datetime型の生成
構文
datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0)
意味
引数で指定した年月日時分秒、マイクロ秒のdatetime型を生成する

datetime型の属性
属性 意味
year 年
month 月
day 日
hour 時
minute 分
second 秒
microsecond マイクロ秒
"""

from datetime import datetime

d = datetime(2021, 10, 12, 12, 1, 5)
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)
