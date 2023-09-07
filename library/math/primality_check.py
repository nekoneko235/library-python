import time

import sympy as sp

# 素数判定
# 計算量：~O(sqrt(N))


def is_prime(N):
    if N == 1:
        return False
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
