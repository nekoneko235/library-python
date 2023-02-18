"""
文字列からtimeへの変換
構文 datetime.strptime("日付文字列", "フォーマット文字列").time()
意味 文字列からdatetimeを生成し、time型に変換する

time型変数から文字列への変換
メソッド time型変数.strftime("フォーマット文字列")
戻り値 time型変数から文字列へ変換して返す

文字列からtimeへの変換は、datetimeのstrptimeメソッドに相当するものがないため、datetimeオブジェクトをいったん生成してからtimeに変換する

一方、timeから文字列への変換はstrftimeメソッドを使用する。引数にフォーマット文字列を指定する
"""

from datetime import datetime

t = datetime.strptime("12:15:05", "%H:%M:%S").time()
time_str = t.strftime("%H.%M.%S")
print(time_str)
