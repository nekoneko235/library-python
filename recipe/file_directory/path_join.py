"""
os.path.join(パス1, パス2...) 結合したパス

os.path.join
- 引数で指定したパスを結合することが可能
- 引数に対し順番で結合したいパス文字列を指定する

パス結合の注意点
- Unix系の場合、結合先に/が先頭のパスが指定されると、ルートからのパスとみなされ階層がリセットされるので注意
"""

import os.path

suzuki_home = os.path.join('.', 'suzuki', 'dir')
print(suzuki_home)

# dirの前にスラッシュが付いているため、前2つのパスが無視され
# 結合結果が/dirとなっている
suzuki_home = os.path.join('.', 'suzuki', '/dir')
print(suzuki_home)
