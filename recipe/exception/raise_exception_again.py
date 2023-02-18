"""
例外が発生した際に何かしらの処理をした後、処理を停止させたり呼び出し元で再び例外処理をしたい場合は、例外を再送出させる。
except~asで補足した例外オブジェクトを、raiseを使用して再送出することができる
"""


def div_num(a, b):
    try:
        val = a/b
        print(val)
    except Exception as e:
        print("例外が発生しました。呼び出し元で処理してください。")
        raise e


div_num(7, 0)
