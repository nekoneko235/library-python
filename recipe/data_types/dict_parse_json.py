"""
辞書からJSON文字列への変換
関数
json.dumps(dict型変数, indent=インデント数, ensure_ascii=False)
戻り値
指定した辞書をJSON文字列に変換する

indentを指定すると、視認性を上げるためのインデント数を指定することが可能。また、デフォルトでは日本語などの文字列がユニコードエスケープされるが、ensure_ascii=Falseを指定するとそのままの形式で出力される
"""

import json

data_dict = {'colors': ['red', 'green', 'blue'],
             'items': [123, 456, 789],
             'users': [{'name': '鈴木', 'id': 1},
                       {'name': '佐藤', 'id': 5}]}

json_str = json.dumps(data_dict, indent=2, ensure_ascii=False)
print(json_str)
