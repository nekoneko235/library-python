import math

import numpy as np
import sympy as sp

# 最大公約数(速度差はない)
x = math.gcd(67280421310722, 67280421310723, 67280421310721)

x = np.gcd.reduce([67280421310723, 67280421310722, 67280421310721])

x = sp.gcd(67280421310723, 67280421310721)  # 3つ以上の引数は不可

# 最小公倍数
x = math.lcm(67280421310722, 67280421310723, 67280421310721)

x = np.lcm.reduce([67280421310723, 67280421310722, 67280421310721])

x = sp.lcm(67280421310723, 67280421310721)  # 3つ以上の引数は不可

# 015 - Caluculate GCD - AtCoderだとPure Python >> NumPy >> SymPy(TLE) の順に速い
# https://atcoder.jp/contests/math-and-algorithm/submissions/45338916
# https://atcoder.jp/contests/math-and-algorithm/submissions/45338898
# https://atcoder.jp/contests/math-and-algorithm/submissions/45338934

# 016 - Greatest Common Divisor of N integers - AtCoderだとPure Python >> NumPy の順に速い
# https://atcoder.jp/contests/math-and-algorithm/submissions/45339087
# https://atcoder.jp/contests/math-and-algorithm/submissions/45339095

# 017 - Least Common Multiple of N integers - AtCoderだとPure Python >> NumPy の順に速い
# https://atcoder.jp/contests/math-and-algorithm/submissions/45339165
# https://atcoder.jp/contests/math-and-algorithm/submissions/45339194

# Python (CPython 3.11.4) だと NumPy, SymPy で ある程度速度が出る
