import time

import sympy as sp

# 素数判定
# 計算量：~O(sqrt(N))


# 2以上の整数Nが素数かどうかを判定する
def is_prime(N):
    LIMIT = int(N**0.5)
    for i in range(2, LIMIT + 1):
        if N % i == 0:
            return False
    return True


# SymPy > Pure Python の順に高速
time_start = time.time()
x = is_prime(67280421310721)
# x = sp.isprime(170141183460469231731687303715884105727)
time_end = time.time()
print(f"Time: {time_end - time_start:.3f} sec")

time_start = time.time()
x = sp.isprime(67280421310721)
# x = sp.isprime(170141183460469231731687303715884105727)
time_end = time.time()
print(f"Time: {time_end - time_start:.3f} sec")

# 011 - Print Prime Numbers - AtCoderだとPure Pythonの方が速い(SymPyは激遅TLE)
# https://atcoder.jp/contests/math-and-algorithm/submissions/45338049
# https://atcoder.jp/contests/math-and-algorithm/submissions/45338025

# 012 - Primality Test - AtCoderだとPure Pythonの方が速い(SymPyは激遅)
# https://atcoder.jp/contests/math-and-algorithm/submissions/45338113
# https://atcoder.jp/contests/math-and-algorithm/submissions/45338098

# Python (CPython 3.11.4) だと NumPy, SymPy で ある程度速度が出る
