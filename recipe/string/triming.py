# 文字列の両側をトリミングした文字列
text = " abcdefg "
stripped = text.strip()
print("*" + stripped + "*")

text = " abcdefg "

# 右側の空白を除去
r_stripped = text.rstrip()
print("*" + r_stripped + "*")

# 左側の空白を除去
l_stripped = text.lstrip()
print("*" + l_stripped + "*")
