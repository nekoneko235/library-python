"""
assert 条件式, メッセージ
条件式が偽の場合、メッセージを出力してAssertionError発生

実行時に想定している条件が満たされていない場合、例外を発生させて処理を中断する機能をアサーションと呼び、不具合の発見に役立てることができる
"""


def sum_abs(x, y):
    """ 2つの数の絶対値の和を求める（バグあり） """
    val = abs(x) + y
    assert val >= 0, "計算結果がマイナスです"
    return val


val1 = sum_abs(-200, 100)
print(val1)
val2 = sum_abs(100, -200)
print(val2)
