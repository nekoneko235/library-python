# lambda式とは、一時的に利用する無名関数を短く記述する方法
func = lambda x: "[" + str(x) + "]"
print(func("ELTE"))

# 高階関数との併用
fruits_list = ["Banana", "Apple", "Orange"]
for fruit in map(lambda x: "[" + str(x) + "]", fruits_list):
    print(fruit)
