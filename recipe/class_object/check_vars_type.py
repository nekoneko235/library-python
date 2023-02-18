"""
type(変数) 引数で指定した変数の型が返される
isinstance(変数, 型) 引数が指定した型もしくはそのサブクラスの場合、Trueが返される
"""
# type関数

x = 100
print(type(x))

lst = [1, 2, 3]
print(type(lst))

text = "abc"
print(type(text))


class Sample:
    pass


s = Sample()
print(type(s))
