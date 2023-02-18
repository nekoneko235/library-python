"""
空白行の削除
[line for line in text.split("\n") if line.strip() != ""]
"""

text = """The Zen of Python, by Tim Peters

Beautifull is better than ugly.

Explicit is better than implicit.

"""

lines = text.split("\n")
line_list = [line for line in lines if line.strip() != ""]
new_text = "\n".join(line_list)
print(new_text)
