"""
dir(変数) 変数が持つ属性がリストとして返される
hasattr(変数, "属性の文字列") 変数が指定した属性を持つ場合Trueが返される

"""


class Sample:
    def __init__(self, x, y):
        self.x = x
        self.y = y


s = Sample(1, 2)
print(dir(s))

print(hasattr(s, 'x'))
print(hasattr(s, 'z'))
