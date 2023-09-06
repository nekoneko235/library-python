import numpy as np
import sympy as sp

# 階乗
# 計算量：~O(N)


def factorial(N):
    # MOD = 10**9 + 7
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        # fact[i] = i * fact[i - 1] % MOD
        fact[i] = i * fact[i - 1]
    return fact[N]


# 自作, math, numpy, sympyの速度はほぼ変わらない
x = factorial(10000)

x = np.math.factorial(10000)

x = sp.factorial(10000)
