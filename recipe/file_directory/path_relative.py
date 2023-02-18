"""
os.path.relpath(パス, 起点となるパス)
- os.path.relpathで指定したパス間の相対パスを得ることができる
"""

import os

print(os.path.relpath(r"./tmp.txt", r"/home"))
