"""
辞書のマージ

updateメソッドによるマージ
dict型変数1.update(dict型変数2)
- dict型変数1にdict型変数2の要素をマージする。戻り値なし
キーに重複がある場合は引数で指定した辞書の値が優先される
元の辞書自体が変更されるという点に注意

dictによる新たなマージされた辞書の生成
dict(dict型変数1, **dict型変数2)
- dict型変数1にdict型変数2の要素をマージした新たな辞書を返す
"""

d1 = {"key1": 100, "key2": 200}
d2 = {"key2": 220, "key3": 300, "key4": 400}

d1.update(d2)  # d1にd2をマージ
print(d1)

d1 = {"key1": 100, "key2": 200}
d2 = {"key2": 220, "key3": 300, "key4": 400}

d3 = dict(d1, **d2)
print(d3)