"""
os.remove(削除対象パス)
- 指定したパスのファイルを削除する。戻り値なし
shutil.rmtree(削除対象パス)
- 指定したパスの配下を含め削除する。戻り値なし
"""

import os

os.remove(r'tmp.txt')
