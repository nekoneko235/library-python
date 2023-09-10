import time

import sympy as sp

# 素因数分解
# 計算量：~O(sqrt(N))


def prime_factorization(N):
    primes = []
    LIMIT = int(N**0.5)
    for i in range(2, LIMIT + 1):
        if N % i == 0:
            ex = 0
            while N % i == 0:
                ex += 1
                N //= i
            primes.append([i, ex])
    if N >= 2:
        primes.append([N, 1])
    return primes


# SymPy >> Pure Python の順に高速
time_start = time.time()
primes = prime_factorization(10**16 + 781222)
print(primes)
time_end = time.time()
print(f"Time: {time_end - time_start:.3f} sec")


# SymPy
time_start = time.time()
primes = sp.factorint(10**16 + 781222)
print(primes)
time_end = time.time()
print(f"Time: {time_end - time_start:.3f} sec")

# 014 - Factorization - AtCoderだとPure Pythonの方が速い(SymPyは激遅)
# https://atcoder.jp/contests/math-and-algorithm/submissions/45338322
# https://atcoder.jp/contests/math-and-algorithm/submissions/45338382

# Python (CPython 3.11.4) だと NumPy, SymPy で ある程度速度が出る
