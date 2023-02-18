"""
関数内部に関数を定義することが可能
関数内部に定義した関数を内部関数と呼ぶ
"""


def outer_function():
    """ 外側の関数 """
    print('outer_function実行')

    def inner_function():
        """ 内側の関数 """
        print('inner_function実行')

    inner_function()


outer_function()
