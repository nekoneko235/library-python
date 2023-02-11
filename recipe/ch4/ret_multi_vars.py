# 戻り値をカンマ区切りで列挙することにより、複数の値を返す
# 原理的にはreturnで列挙した値がタプルとして返され、
# アンパックにより呼び出し側で列挙した変数に展開され、格納

def func(x, y):
    return x + y, x - y


a, b = func(2, 3)
print(a, b)
