"""
float型には、float関数の引数にinfを指定して無限大を表現することが可能
また、infは演算することができる
また、float関数の引数にnanを指定して非数（Not a Number）を表現することも可能で、
inf同士の演算で値が不定のときなどの結果として使用される場合もある
"""
x = float("inf")
y = -float("inf")

z1 = x + 100
z2 = x + y
z3 = x / y

print(z1)
print(z2)
print(z3)
