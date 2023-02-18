"""
文字列とdate型の変換

文字列からdateへ変換する場合、date型にはdatetimeのstrptimeメソッドに相当するものがないため、datatimeオブジェクトをいったん生成してからdateに変換する

一方、dateから文字列に変換する場合は、datetime型と同様strftimeメソッドを使用する
"""

from datetime import datetime

# 文字列からdatetime型さらにdate型に変換
d = datetime.strptime("2021/10/12", "%Y/%m/%d").date()

# date型から文字列に変換
date_str = d.strftime("%Y-%m-%d")
print(date_str)
