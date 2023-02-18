"""
構文
date(year, month, day)
意味
引数で指定した年月日のdate型を生成する

date型の属性
year 年
month 月
day 日
"""

from datetime import date

d = date(2021, 10, 12)
print(d.year)
print(d.month)
print(d.day)
