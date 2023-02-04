# 曜日の辞書を生成する
week_days ={'Monday': '月曜日', 'Tuesday': '火曜日', 'Wednesday': '水曜日', 'Thursday': '木曜日', 'Friday': '金曜日', 'Saturday': '土曜日', 'Sunday': '日曜日'}
print(week_days)

# 空の辞書を生成
empty = {}

# dict()による辞書の生成
week_days_list = [["Monday", "月曜日"], ["Tuesday", "火曜日"], ["Wednesday", "水曜日"], ["Thursday", "木曜日"], ["Friday", "金曜日"], ["Saturday", "土曜日"], ["Sunday", "日曜日"]]
week_days_dict = dict(week_days_list)
print(week_days_dict)

# キーの存在判定
d = {"key1": 100, "key2": 200}
b = ("key1" in d.keys())
print(b)

# 値の存在判定
d = {"key1": 100, "key2": 200}
b = (200 in d.values())
print(b)

# キーと値の組の存在判定
d = {"key1": 100, "key2": 200}
b = (("key2", 200) in d.items())
print(b)
