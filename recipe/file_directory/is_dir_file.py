"""
os.path.isdir(パス)
- 指定したパスがディレクトリの場合True, それ以外はFalse
os.path.isfile(パス)
- 指定したパスがファイルの場合True, それ以外はFalse
"""

import os.path

print(os.path.isdir(r"/home"))
print(os.path.isdir(r"/home/kenny/atcoder_python/task.py"))
print(os.path.isfile(r"/home"))
print(os.path.isfile(r"/home/kenny/atcoder_python/task.py"))
