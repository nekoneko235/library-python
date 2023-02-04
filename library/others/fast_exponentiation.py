# 繰り返し二乗法
# Pythonには「a^NをMで割った余り」を計算できる関数pow()が標準で存在する
# 計算量：O(logN)

N = int(input())
MOD = 10**9+7
ans = pow(3, N, MOD)
print(ans)
