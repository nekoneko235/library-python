# イテラブルな変数を同時にループ処理できるイテレータを得る
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x, y in zip(list1, list2):
    print(x, y)

# 2つ以上指定できる
# 要素数が異なる場合は一番少ない要素数に合わされる
list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3]
list3 = ["A", "B", "C", "D", "F"]
for x, y, z in zip(list1, list2, list3):
    print(x, y, z)
