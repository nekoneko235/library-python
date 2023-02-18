"""
構文 意味
str型変数1 in str型変数2 str型変数1の文字列がstr型変数2の文字列に含まれる場合はTrue

大文字小文字全角半角は、厳密に区別される
"""

text = "This is a pen"
contains = "pen" in text
print(contains)

"""
大文字小文字を区別したくない場合は、いったんどちらかにすべて置換する
"""

text = "This is a pen."
contains = "THIS".lower() in text.lower()
print(contains)
