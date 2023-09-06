import math
import time

import sympy as sp

# 二項係数 nCk
# パスカルの三角形を用いる
# 計算量：~O(N)


def n_choose_k(N):
    C = []
    for i in range(N + 1):
        C.append([0] * (N + 1))
    C[0][0] = 1
    MOD = 10**9 + 7
    for i in range(1, N + 1):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
            C[i][j] %= MOD
    return C


# 自作が一番遅い, math, sympyの速度はほぼ変わらない
time_start = time.time()
C = n_choose_k(1000)
time_end = time.time()
print(f"Time: {time_end - time_start:.3f} sec")

time_start = time.time()
x = math.comb(100000, 7777)
time_end = time.time()
print(f"Time: {time_end - time_start:.3f} sec")

time_start = time.time()
x = sp.binomial(100000, 7777)
time_end = time.time()
print(f"Time: {time_end - time_start:.3f} sec")
