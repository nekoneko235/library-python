import os


app_env = os.environ.get("APP_ENV")
if app_env == 'DEV':
    print("開発環境")
elif app_env == 'PROD':
    print("本番環境")
else:
    print("設定されていない")
