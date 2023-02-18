"""
辞書のキーとして使用できるのはhashableという性質を持った型の変数
int型
str型
tuple型
"""

"""
辞書の値の参照方法は2種類ある
1. []を使用した参照
    - キーが存在しない場合はKeyError発生
2. getメソッドを使用した参照
    2.1. キーが存在しない場合はNoneが返される
    2.2. キーが存在しない場合は引数で設定したデフォルト値が返される
"""

d = {"key1": 100, "key2": 200}
val = d["key2"]  # KeyErrorが発生
val = d["key1"]
print(val)

d = {"key1": 100, "key2": 200}
# 存在するキーを指定
val1 = d.get("key1")
print(val1)
# 存在しないキーを指定
val2 = d.get("key3")
print(val2)
val3 = d.get("key3", 999)
print(val3)


# 曜日の辞書を生成する
week_days = {'Monday': '月曜日', 'Tuesday': '火曜日', 'Wednesday': '水曜日',
             'Thursday': '木曜日', 'Friday': '金曜日',
             'Saturday': '土曜日', 'Sunday': '日曜日'}
print(week_days)

# 空の辞書を生成
empty = {}

# dict()による辞書の生成
week_days_list = [["Monday", "月曜日"], ["Tuesday", "火曜日"],
                  ["Wednesday", "水曜日"], ["Thursday", "木曜日"],
                  ["Friday", "金曜日"], ["Saturday", "土曜日"], ["Sunday", "日曜日"]]
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
