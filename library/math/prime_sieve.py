import time

import numpy as np

# import sympy as sp

# エラトステネスの篩
# 計算量：~O(N log(log(N)))


def sieve_of_Eratosthenes(N):
    primes = [True] * (N + 1)
    res = []

    # エラトステネスの篩
    LIMIT = int(N**0.5)
    for i in range(2, LIMIT + 1):
        if primes[i]:
            # x = 2i, 3i, 4i, ... と篩落とす
            for j in range(2 * i, N + 1, i):
                primes[j] = False

    # N 以下の素数を小さい順に res配列に追加
    res = [i for i in range(2, N + 1) if primes[i]]
    return res


def sieve_of_Eratosthenes_numpy(N):
    primes = np.ones(N + 1, dtype=bool)
    primes[:2] = False  # 0, 1 は素数ではない

    LIMIT = int(N**0.5) + 1

    for i in range(2, LIMIT):
        if primes[i]:
            primes[i * 2 :: i] = False

    return np.nonzero(primes)[0]


# NumPy >> Pure Python >> SymPy の順に高速
time_start = time.time()
# arr = sieve_of_Eratosthenes(10**8)
# print(arr)
time_end = time.time()
print(f"Time: {time_end - time_start:.3f} sec")

# Numpy
time_start = time.time()
arr = sieve_of_Eratosthenes_numpy(10**8)
# print(arr)
time_end = time.time()
print(f"Time: {time_end - time_start:.3f} sec")

# SymPy (2を除く素数を返す)
time_start = time.time()
# primes = list(sp.primerange(10**6))
# print(primes)
time_end = time.time()
print(f"Time: {time_end - time_start:.3f} sec")


# 11 - Print Prime Numbers - AtCoderだとPure Python >> NumPy >> SymPyの順に高速
# https://atcoder.jp/contests/math-and-algorithm/submissions/45430930
# https://atcoder.jp/contests/math-and-algorithm/submissions/45430957
# https://atcoder.jp/contests/math-and-algorithm/submissions/45430987
