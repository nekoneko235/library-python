"""
shutil.copy(コピー前パス, コピー後パス)
- 指定したファイルをコピーし、コピー先のパスを文字列で返す
shutil.copytree(コピー前パス, コピー後パス)
- 指定したパスをディレクトリごとコピーし、コピー先のパスを文字列で返す
"""

import shutil

shutil.copy(r"tmp.txt", r"tmp2.txt")
