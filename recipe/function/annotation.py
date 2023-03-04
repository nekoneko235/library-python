# 変数アノテーションを利用すると、利用する型を読み手に伝える
# 関数にも変数と同様にアノテーションをつけることができ、
# 引数、戻り値の型などを記述することができる
# アノテーションはあくまでも注釈であるため型チェックは行わない

# 変数アノテーション
val: int = 100
text: str = "abcdefg"


# 関数アノテーション
def func(num: int, unit: str) -> str:
    return str(num) + unit


text = func(100, "円")
print(text)


# 型を記述する
def func(num: int, unit: str) -> str:
    return str(num) + unit


text = func(100, "円")
print(text)
