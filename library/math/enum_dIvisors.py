import time

import numpy as np
import sympy as sp

# 約数列挙
# 計算量：~O(sqrt(N))


def enum_divisors(N):
    LIMIT = int(N**0.5)
    divisors = []
    for i in range(1, LIMIT + 1):
        if N % i == 0:
            divisors.append(i)
            if i != N // i:
                divisors.append(N // i)
    return divisors


# SymPy >>>> Pure Python の順に高速
time_start = time.time()
divs = enum_divisors(10**12)
time_end = time.time()
print(f"Time: {time_end - time_start:.3f} sec")


# SymPy
time_start = time.time()
divs = sp.divisors(10**12)
time_end = time.time()
print(f"Time: {time_end - time_start:.3f} sec")
