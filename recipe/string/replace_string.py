"""
メソッド 戻り値
str型変数.replace(old, new) 文字列のoldをnewに置換した文字列
str型変数.replace(old, new, count) 文字列のoldをnewにcountで指定した回数置換した文字列

戻り値で置換後の文字列が得られ、元の文字列自体は更新されない
"""

text1 = "Simple is better than complex."
text2 = text1.replace(' ', '_')
print(text1)
print(text2)
