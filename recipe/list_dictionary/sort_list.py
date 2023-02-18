"""
関数 戻り値
sorted(list型変数)
- 引数で指定したリストをソートした新たなリストを返す

メソッド 処理と戻り値
list型変数.sort()
- リスト自身をソートする。戻り値なし
"""

l1 = ['bc', 'ac', 'bD', 'AB']
l2 = sorted(l1)
print(l2)

# 大文字/小文字を区別せずにソートする
l2 = sorted(l1, key=str.lower)
print(l2)

l1.sort()
print(l1)

# 大文字/小文字を区別せずにソートする
l1.sort(key=str.lower)
print(l2)
