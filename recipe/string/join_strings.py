"""
メソッド 戻り値
"区切り文字".join([文字列1, 文字列2, ...]) 区切り文字で文字列1, 文字列2 ... を連結した文字列
"""

text_list = ['abc', 'def', 'ghi']
test1 = ''.join(text_list)
print(test1)
test2 = ','.join(text_list)
print(test2)
