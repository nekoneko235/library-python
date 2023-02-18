"""
中括弧単体
formatメソッドの引数に埋め込みたい値を列挙する
"""

text = "こんにちは、{}さん。現在{}時です。"
name = "Suzuki"
time = 10

ftext = text.format(name, time)
print(ftext)


"""
フィールド番号
フィールド番号付きの場合、formatメソッドの引数は中括弧単体のときと同様に、値を列挙するが、引数の順序とフィールド番号が対応づけられる
"""

text = "こんにちは、{0}さん。現在{1}時です。"
name = "Suzuki"
time = 10

ftext = text.format(name, time)
print(ftext)


"""
フィールド名
フィールド番号付きの場合、formatメソッドの引数にキーワードで指定する
"""

text = "こんにちは、{name}さん。現在{time}時です。"
name = "Suzuki"
time = 10

# キーワード引数
ftext1 = text.format(name=name, time=time)
print(ftext1)
