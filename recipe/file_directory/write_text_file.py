"""
f.write(文字列) 指定した文字列を書き込み書き込まれた文字数を返す
f.writelines(文字列リスト) 指定した文字列リストを1つずつ書き込み。戻り値なし
"""

text = "aaa\nbbb\nccc"
with open("tmp.txt", "w") as f:
    f.write(text)
