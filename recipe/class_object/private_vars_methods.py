"""
変数やメソッドの頭にアンダーバーを2つつけることにより、外部からのアクセスを抑制することができる
"""


class Sample():
    def __init__(self, val1):
        self.__instance_val1 = val1

    def __private_method(self):
        print(self.__instance_val1)


s = Sample(10)
# print(s.__instance_val1)
# AttributeError: 'Sample' object has no attribute '__instance_val1'
# s.__private_method()
# AttributeError: 'Sample' object has no attribute '__private_method'
