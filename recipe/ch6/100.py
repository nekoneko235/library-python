import traceback


try:
    x = 1/0
except Exception:
    # 文字列を取得する format_exc関数
    print("エラー情報\n" + traceback.format_exc())
