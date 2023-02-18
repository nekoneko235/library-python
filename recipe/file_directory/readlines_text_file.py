"""
readlines
- 1行ずつ区切ったリストが得られる
- 1行ずつ処理したい場合に利用できる
"""


with open("tmp.txt", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    print(str(i) + ":" + line, end="")
