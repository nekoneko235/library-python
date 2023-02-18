"""
os.path.exists(パス) 存在する場合はTrue, 存在しない場合はFalse
"""

import os.path

if os.path.exists(r"/home/kenny/atcoder_python/note.php"):
    print("File exists")
else:
    print("Does not exist")
