"""
特定行の抽出
[line for line in text.split("\n") if "特定の文字列" in line]
"""

text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
"""

lines = text.split("\n")
line_list = [line for line in lines if "com" in line]
new_text = "\n".join(line_list)
print(new_text)
