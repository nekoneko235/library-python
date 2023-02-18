"""
raise 例外クラス もしくは例外オブジェクト
    指定した種類の例外を発生

raiseで指定できる例外は、Exceptionを継承した例外クラスと例外オブジェクトとなる。例外オブジェクトは例外クラスをインスタンス化したもの
"""


import numbers


def calc10times(num):
    if not isinstance(num, numbers.Number):
        raise TypeError('パラメータが不正です')

    return num * 10


val = calc10times(10)
print(val)
val = calc10times('abc')
print(val)
