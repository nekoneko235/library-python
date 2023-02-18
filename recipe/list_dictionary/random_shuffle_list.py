"""
リストのランダムシャッフル

関数 処理と戻り値
random.sample(list型変数, len(list型変数))
- 引数で指定されたリストをシャッフルした新たなリストを返す
random.shuffle(list型変数)
- 引数で指定されたリストをシャッフルする。戻り値なし
"""

import random

l1 = [0, 1, 2, 3, 4]
l2 = random.sample(l1, len(l1))
print(l2)

l1 = [0, 1, 2, 3, 4]
random.shuffle(l1)
print(l1)
