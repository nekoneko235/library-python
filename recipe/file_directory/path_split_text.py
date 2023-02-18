"""
os.path.splittext(パス)
- 指定したパスの拡張子の手前までと拡張子のタプル
"""

import os.path

root, ext = os.path.splitext(r"/home/kenny/atcoder_python/task.py")
print(root, ext)
