# リスト
l = ['a', 'b', 'c']
for idx, val in enumerate(l):
    if idx != 0:
        print(idx, val)

# 辞書のitemsとの併用
d = {'key1': 110, 'key2': 220, 'key3':330}
for idx, (key, value) in enumerate(d.items()):
    print(idx, key, value)
