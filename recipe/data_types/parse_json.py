"""
JSON文字列を辞書に変換
関数
json.loads(JSON文字列)
戻り値
JSON文字列をパースした結果を格納した辞書
"""

import json

json_text = """
{
    "colors": ["red", "green", "blue"],
    "items": [123, 456, 789],
    "users": [
        {"name": "鈴木", "id": 1},
        {"name": "佐藤", "id": 5}
    ]
}
"""

data_dict = json.loads(json_text)

# 結果辞書全体を表示
print(data_dict)

# colorsキーを指定して0番目を取得
print(data_dict["colors"][0])

# usersキーを指定、0番目のidを取得
print(data_dict["users"][0]["id"])
