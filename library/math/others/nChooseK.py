# 二項係数 nCk
# パスカルの三角形を用いる
# 計算量：~O(N)

N = int(input())
C = []
for i in range(N+1):
    C.append([0]*(N+1))
C[0][0] = 1
MOD = 10**9+7
for i in range(1, N+1):
    C[i][0] = 1
    for j in range(1, i+1):
        C[i][j] = C[i-1][j-1] + C[i-1][j]

# C[n][k]
# print(C[3][2])
