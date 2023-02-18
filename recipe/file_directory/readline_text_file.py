"""
readline
- 1行ずつ内容を返す
- ファイル終端に達すると空文字列を返す
"""


with open("tmp.txt", "r") as f:
    print(f.readline(), end="")
    print(f.readline(), end="")
    print(f.readline(), end="")
    print(f.readline(), end="")
