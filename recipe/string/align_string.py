"""
メソッド 戻り値
str型変数.rjust(文字数, 埋める文字)
- 指定した文字および文字数で右寄せした文字列
"""

text = "abc"

# 右寄せ
rjust_text = text.rjust(6, '*')
print(rjust_text)

# 左寄せ
ljust_text = text.ljust(6, '*')
print(ljust_text)

# 中央寄せ
centralized_text = text.center(6, '*')
print(centralized_text)
