"""
traceback.format_exc() 発生した例外の詳細情報の文字列
"""

import traceback


try:
    x = 1/0
except Exception:
    # 文字列を取得する format_exc関数
    print("エラー情報\n" + traceback.format_exc())
