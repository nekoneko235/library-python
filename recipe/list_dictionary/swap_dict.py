"""
辞書内包表記によるキーと値の入れ替え
{value:key for key, value in dict型変数.items()}

ただし、辞書の特性上キーはユニークかつhashableであることが求められるため、この構文を使用する場合は辞書の値もユニークかつhashableであることが前提として求められる
"""

d = {'key1': 100, 'key2': 200, 'key3': 300}
swapped_dict = {value: key for key, value in d.items()}
print(swapped_dict)
