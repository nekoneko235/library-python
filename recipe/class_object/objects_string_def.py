"""
str(変数)  オブジェクトの表示用文字列
repr(変数) オブジェクト情報を表した文字列

strは表示用の簡易版文字列表現
reprはオブジェクト情報を表した正式版という位置づけ

__str__メソッドで実装する。文字列表現を得る場合はstr関数で呼び出す。print関数を利用する場合はstr関数の呼び出しを省略できる
__repr__メソッドで実装する。文字列表現を得る場合はrepr関数で呼び出す。公式ドキュメントでは「同じ値のオブジェクトを再生成するのに使える、有効なPython式のようなもの」が推奨されている
"""


class User:
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail

    def __str__(self):
        return "ユーザ名:" + self.name + ", メールアドレス:" + self.mail

    def __repr__(self):
        return str({'name': self.name, 'age': self.mail})


user = User("Suzuki", "suzuki@example.com")
print(user)
print(repr(user))
