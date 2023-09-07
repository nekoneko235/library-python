import time

# 繰り返し二乗法
# Pythonには「N^XをMで割った余り」を計算できる関数pow()が標準で存在する
# 計算量：O(logN)

N = 2
X = 10
MOD = 10**9 + 7

# Pure Python で十分高速
time_start = time.time()
ans = pow(N, X, MOD)
print(ans)
time_end = time.time()
print(f"Time: {time_end - time_start:.3f} sec")
