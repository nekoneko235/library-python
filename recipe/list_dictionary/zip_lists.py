"""
キーと値のリストから辞書を生成
dict(zip(キーのリスト, 値のリスト))

zip関数を使用すると、複数のイテラブルな変数をまとめたイテレータを得ることができる。これを利用してキーと値のリストから辞書を生成することができる
"""

keys = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']
values = ['月曜日', '火曜日', '水曜日',
          '木曜日', '金曜日', '土曜日', '日曜日']

week_days = dict(zip(keys, values))
print(week_days)
