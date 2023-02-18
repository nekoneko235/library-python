"""
logging.basicConfigの引数formatにフォーマット文字列を指定することで、ログのフォーマットを設定することができる

変数    意味
%(name)s       logger名
%(levelno)s    ログレベル番号
%(levelname)s  ログレベル名
%(pathname)s   (利用可能であれば)ソースファイルのフルパス
%(filename)s   ソースファイル名
%(module)s     モジュール名
%(lineno)d     (利用可能であれば)行番号
%(funcName)s   関数、メソッド名
%(asctime)s    LogRecordが作成された時間のテキスト形式
%(thread)d     (利用可能であれば）スレッドID
%(threadName)s (利用可能であれば）スレッド名
%(process)d    (利用可能であれば）プロセスID
%(message)s    メッセージ
"""
