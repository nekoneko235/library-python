"""
文字列 意味
%Y 西暦4桁
%m 2桁でゼロ埋めした月
%d 2桁でゼロ埋めした日
%H 2桁でゼロ埋めした時（24時間表記）
%M 2桁でゼロ埋めした分
%S 2桁でゼロ埋めした秒
%f 6桁でゼロ埋めしたマイクロ秒
"""

from datetime import datetime

# 文字列からdatetime型を生成
dt = datetime.strptime("2021/10/12 12:05:00",
                       "%Y/%m/%d %H:%M:%S")

# datetime型から文字列に変換
datetime_str = dt.strftime("%Y-%m-%d %H:%M:%S")
print(datetime_str)
