"""
メソッド 戻り値
str型変数.isalnum()   すべての文字が英数字でかつ1文字以上であるならTrue
str型変数.isalpha()   すべての文字が英字でかつ1文字以上であるならTrue
str型変数.isascii()   すべての文字がASCⅡか、空文字の場合True
str型変数.isdecimal() すべての文字が10進数の数字でかつ1文字以上あるならTrue
str型変数.islower()   すべての文字が小文字でかつ1文字以上あるならTrue
str型変数.isupper()   すべての文字が大文字でかつ1文字以上あるならTrue
str型変数.isspace()   すべての文字が空白文字でかつ1文字以上あるならTrue
"""

text1 = "abc123"
text2 = "123"

# ASCIIのみかどうか
print(str.isascii(text1))
print(str.isascii(text2))

# 10進数の数字のみかどうか
print(str.isdecimal(text1))
print(str.isdecimal(text2))

print(str.isalnum("ａｂｃ１２３"))
print(str.isalpha("ａｂｃ"))
print(str.isdecimal("１２３"))
print(str.isspace("　"))  # 全角のスペース
