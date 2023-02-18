"""
set型
順序を持たない
重複要素を持たない
"""

s = {1, 3, 5, 7}
s = set([1, 2, 3, 1, 2, 3])
print(s)

# 空のset型を生成
empty = set()

# 要素の追加
s.add(4)
s.add(8)
s.add(10)

# 要素の削除
s.remove(4)
s.remove(8)

# 存在判定
print(4 in s)
print(8 in s)
print(10 in s)

# 全部削除
s.clear()

print(s)
