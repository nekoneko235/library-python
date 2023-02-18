import logging

"""
ログハンドラの設定
logging.basicConfig(handlers=[ハンドラ1, ハンドラ2, ....])

代表的なログハンドラ
ハンドラ ハンドラの生成 出力先
StreamHandler logging.StreamHandler() 標準出力
FileHandler logging.FileHandler("出力先パス") ファイル出力

ログハンドラ
ログの出力先には、標準出力以外にもファイルに出力することが可能
出力先を設定する場合、組み込みで用意されているハンドラを指定する
例えば標準出力とファイル出力をしたい場合は、ハンドラを2つ生成して指定することになる

"""

# ハンドラを生成する
std_handler = logging.StreamHandler()
file_handler = logging.FileHandler("tmp.log")

# フォーマット、ログレベル、ハンドラを設定する
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message\
)s', level=logging.DEBUG, handlers=[std_handler, file_handler])

logger = logging.getLogger(__name__)
logger.debug("デバッグ出力")
logger.debug("情報出力")
logger.debug("警告発生！")
logger.debug("エラー発生!!")
