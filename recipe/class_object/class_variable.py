"""
クラス変数は、オブジェクト生成しなくても利用できるクラスに属する変数のこと
インスタンス変数と異なり、class分ブロックの直下に変数定義を記述する
"""


class Sample():
    class_val1 = 1
    class_val2 = 2

    def __init__(self):
        pass


print(Sample.class_val1, Sample.class_val2)

# クラス変数は代入により変更することができる
Sample.class_val2 = 999
print(Sample.class_val1, Sample.class_val2)

s = Sample()

# クラス変数が参照できる
print(s.class_val1, s.class_val2)

# 代入しようとする
s.class_val1 = 100

# 新たにインスタンス変数class_val1が設定される
# インスタンスからクラス変数にアクセスできなくなる
print(s.class_val1, Sample.class_val1)
