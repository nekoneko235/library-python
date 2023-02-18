"""
import os
変数 = os.environ[環境変数]

本番と開発環境でDBの接続先などを変えたい場合、環境変数を使う方法が挙げられる。環境変数は、osモジュールのos.envirionに辞書形式で取得可能
"""


import os


app_env = os.environ.get("APP_ENV")
if app_env == 'DEV':
    print("開発環境")
elif app_env == 'PROD':
    print("本番環境")
else:
    print("設定されていない")
