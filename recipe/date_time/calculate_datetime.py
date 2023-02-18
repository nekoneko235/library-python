"""
timedelta型の生成
構文
timedelta(days=0, seconds=0, microseconds=0,
milliseconds=0, minutes=0, hours=0, weeks=0)
意味
引数の指定した時間分datetime型、date型に対して演算を行えるtimedelta型を生成する
"""

from datetime import datetime, date, timedelta

# 2021/12/22のdate型を生成
d1 = date(2021, 12, 22)

# 2021/12/22 12:00:30のdatetime型を生成
dt1 = datetime(2021, 12, 22, 12, 00, 30)

# 100日分のtimedelta型を生成
delta = timedelta(days=100)

# 100日後の日付を計算
d2 = d1 + delta
dt2 = dt1 + delta

# 計算結果をprint出力
print(d2)
print(dt2)

d2 = d1 - delta
dt2 = dt1 - delta

print(d2)
print(dt2)
