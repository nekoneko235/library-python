"""
os.path.abspath(パス) 絶対パス文字列
- os.path.abspathで指定した相対パスの絶対パスを得ることができる
"""

import os

print(os.path.abspath(r".\tmp.txt"))
