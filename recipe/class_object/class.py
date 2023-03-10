# クラス定義
class User:
    """ ユーザークラス """

    # メソッドの第1引数にはデフォルトで自動的に自身のオブジェクトが設定され、
    # 通常selfと記述する
    def __init__(self, name, mail):
        """ 初期化処理 """
        self.name = name
        self.mail = mail

    def print_user_info(self):
        """ ユーザー情報をprint出力する """
        print("ユーザ名:" + self.name)
        print("メールアドレス:" + self.mail)


# User型オブジェクト生成
user1 = User("Suzuki", "suzuki@example.com")

# インスタンス変数参照
print(user1.name)

# メソッド利用
user1.print_user_info()

# インスタンス変数を更新する
user1.name = "Sato"
user1.mail = "sato@example.com"

# メソッド利用
user1.print_user_info()
