# モジュール変数は関数内部から参照することが可能

val = 100


def func():
    print(val)


func()

# モジュール変数を更新する場合はglobal宣言を使用する
count = 0


def func():
    global count
    count += 1
    print("実行回数：{}回".format(count))


func()
func()
print("countの値：{}".format(count))
