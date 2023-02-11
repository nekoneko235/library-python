# 辞書内包表記
list1 = [1, 2, 3]
dict2 = {val: 0 for val in list1}
print(dict2)  # {1: 0, 2: 0, 3: 0}

list1 = [1, 2, 3]
dict2 = {val: 0 for val in list1 if val >= 2}
print(dict2)  # {2: 0, 3: 0}

# itemsによる既存の辞書から新たな辞書の生成
d1 = {"key1": 100, "key2": 200, "key3": 300}
d2 = {key: value * 2 for key, value in d1.items()}
print(d2)

# zip関数との併用
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
d = {key: value for key, value in zip(list1, list2)}
print(d)
