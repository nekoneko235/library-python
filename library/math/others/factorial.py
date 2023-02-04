# 階乗
# 計算量：~O(N)

N = int(input())
MOD = 10**9+7
fact = [1]*(N+1)
for i in range(1, N+1):
    fact[i] = i * fact[i-1] % MOD

# print(fact[N])
