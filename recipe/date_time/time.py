"""
time型の生成
構文
datetime.time(hour=0, minute=0, second=0, microsecond=0)
意味
引数で指定した時分秒マイクロ秒のtime型を生成する
"""

from datetime import time

t = time(12, 15, 5)
print(t.hour)
print(t.minute)
print(t.second)
