"""
インスタンスメソッド
def メソッド名(self, 引数):
オブジェクト.メソッド(引数)
=> 生成したオブジェクトから実行できるメソッド。インスタンス変数およびクラス変数にアクセスすることが可能

クラスメソッド
@classmethod
def メソッド名(cls, 引数):
クラス.メソッド(引数)
=> インスタンスを生成することなくアクセスできるメソッドのこと。クラス変数にアクセスすることが可能。\
インスタンス変数にはアクセスできない。クラスメソッドを定義する場合、@classmethodデコレータを付加する。また、第1引数にクラスオブジェクトが自動で設定される。第1引数はclsと記述するのが一般的

スタティックメソッド
@staticmethod
def メソッド名(引数):
クラス.メソッド(引数)
=> インスタンスを生成することなくアクセスできるメソッドのことだが、インスタンス変数にもクラス変数にもアクセスすることができない。\
スタティックメソッドを定義する場合、@staticmethodデコレータを付加する。実質的には関数と同じようなもので、関数を適当なクラスに属させたほうが設計上望ましい場合に使用する。
"""


class Sample():
    class_val1 = 1

    def __init__(self, val1):
        self.instance_val1 = val1

    def instance_method(self):
        print(self.class_val1, self.instance_val1)

    @classmethod
    def class_method(cls):
        print(cls.class_val1)

    @staticmethod
    def static_method():
        local_val = 100
        print(local_val)


# インスタンス・メソッドの呼び出し
s = Sample(10)
s.instance_method()
# クラスメソッドの呼び出し
Sample.class_method()
# スタティックメソッドの呼び出し
Sample.static_method()
