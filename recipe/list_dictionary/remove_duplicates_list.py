"""
重複を除去したリストの作成
list(dict.fromkeys(list型変数))

dict.fromkeys()を使用すると、引数で指定したリストのうち、重複を省いた要素をキーとした辞書を得ることができる

list関数で辞書を指定するとキーのリストが得られるため、これらを合わせることにより重複要素を除去したリストを得ることができる
"""

l1 = [1, 2, 1, 3, 5, 4, 4, 3]
print(dict.fromkeys(l1))
print(list(dict.fromkeys(l1)))
