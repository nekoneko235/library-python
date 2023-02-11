# 1次元DP
# 計算量: ~O(n)
# URL: https://atcoder.jp/contests/dp/tasks/dp_a

# 入力
n = int(input())
H = list(map(int, input().split()))

# 動的計画法
dp = [None]*n
dp[0] = 0
for i in range(1, n):
    if i == 1:
        dp[i] = abs(H[i-1] - H[i])
    if i >= 2:
        v1 = dp[i-1] + abs(H[i-1] - H[i])  # 1 個前の足場からジャンプするとき
        v2 = dp[i-2] + abs(H[i-2] - H[i])  # 2 個前の足場からジャンプするとき
        dp[i] = min(v1, v2)

# 答えの出力
print(dp[n-1])
