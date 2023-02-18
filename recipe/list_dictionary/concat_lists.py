l1 = ["Apple", "Orange", "Banana"]
l2 = ["Mango", "Grape", "Pineapple"]
# l1,l2を結合した結果をl3に代入
# 元のl1,l2には変更はない
l3 = l1 + l2
print(l1)
print(l2)
print(l3)

l1 = ["Apple", "Orange", "Banana"]
l2 = ["Mango", "Grape", "Pineapple"]
# extendを使うとメソッドを実行したリスト自身に変更がある
l1.extend(l2)
print(l1)
