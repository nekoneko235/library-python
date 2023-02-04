# いもす法
# 計算量: ~O(N + Q)
# URL: https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_aj

N, Q = map(int, input().split())
S = [0 for _ in range(N+2)]
for i in range(Q):
    L, R, X = map(int, input().split())
    S[L] += X
    S[R+1] -= X
for i in range(2,N+1):
    if S[i] > 0:
        print("<", end="")
    elif S[i] == 0:
        print("=", end="")
    else:
        print(">", end="")
