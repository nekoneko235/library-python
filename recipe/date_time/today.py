from datetime import date

# todayメソッドで現在のdate型を得ることができる
d = date.today()
d_str = d.strftime("%Y-%m-%d")
print(d_str)
