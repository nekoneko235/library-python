# 通常、関数は実行すると内部の状態はクリアされるが、
# クロージャを使用するとモジュール変数のような global な変数を使用せず、
# 前回実行した内容を記憶させて使用することが可能
# Pythonでは、nonlocalな変数と内部関数を使用してクロージャを実装する

# 戻り値に内部関数を返す関数
def outer_function():
    """ 外側の関数 """

    def inner_function():
        """ 内側の関数 """
        print('inner_functionが実行されました')

    # 内側の関数を変数として返す
    return inner_function

func = outer_function()
func()

# nonlocal宣言とクロージャ
# nonlocal宣言を使用すると、内側で定義した関数から
# 外側のローカル変数を更新することが可能
# nonlocalな変数は、戻り値の関数オブジェクトが利用される間
# そこに実行時の値を保持することができる

def outer_function():
    """ 外側の関数 """

    count = 0

    def inner_function():
        """ 内側の関数 """
        nonlocal count
        count += 1
        print("実行回数：{}回".format(count))

    return inner_function

# 関数オブジェクトを取得
func1 = outer_function()

# 関数を実行
func1()
func1()
func1()
