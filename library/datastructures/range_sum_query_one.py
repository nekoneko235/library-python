# 累積和
# 計算量: ~O(N + Q)
# URL: https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ai

N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = [0 for _ in range(N+1)]
for i in range(N):
    S[i+1] = S[i] + A[i]
for i in range(Q):
    L, R = map(int, input().split())
    print(S[R] - S[L-1])
