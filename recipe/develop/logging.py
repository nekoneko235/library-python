import logging


"""
ログの設定
logging.basicConfig(format="フォーマット文字列", level=ログレベル)

ロガーの取得
logging.getLogger("logger名")

ログレベルとロガーの出力メソッド
低 logging.DEBUG    debug()    デバッグ
|  logging.INFO     info()     情報出力
|  logging.WARNING  warning()  警告出力
|  logging.ERROR    error()    エラー出力
高 logging.CRITICAL critical() 致命的なエラー

logger
loggerはログを出力するオブジェクトで、生成時にlogger名を設定することができる
モジュール名を設定することが多く、その場合は特殊変数__name__を使用する

ログフォーマット
ログには何をどういった形式で出力するか?というフォーマットを定める
こういった出力形式をログフォーマットと呼ぶ
詳しくは 111.py

ログレベル
ログには「レベル」という概念がある
あるログが、無視していいただの情報なのか、エラーなのかといったログ内容の深刻度をレベルで表す
ロガーおよびログハンドラごとに、ログレベルを設定することが可能
デフォルトでは警告レベル以上のログが出力される

ハンドラ
ログの出力先には標準出力やファイル等が設定できる
デフォルトでは標準出力に出力される
詳しくは 112.py
"""

# 以下のサンプルコードは、以下のフォーマットでレベルがINFO以上のログに対しログを標準出力する
# 時間 - ロガー名 - ログレベル - ログメッセージ
logging.basicConfig(format='%(asctime)s - %(name)s - \
                            %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
# 出力レベルをINFO以上に設定しているため、DEBUGログは出力されない
logger.debug("デバッグ出力")
logger.info("情報出力")
logger.warning("警告発生!")
logger.error("エラー発生!!")
