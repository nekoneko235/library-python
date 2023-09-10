# 深さ優先探索
# 計算量：~O(N + M)

import sys

sys.setrecursionlimit(10**9)


def dfs(pos, visited):
    visited[pos] = True
    for nex in G[pos]:
        if not visited[nex]:
            dfs(nex, visited)


# 入力
N, M = map(int, input().split())
G = [[] for _ in range(N)]

# 隣接リストの作成
# 0-indexed
for _ in range(M):
    A, B = map(int, input().split())
    G[A - 1].append(B - 1)
    G[B - 1].append(A - 1)

# 深さ優先探索の初期化
visited = [False] * N

# 深さ優先探索
dfs(0, visited)

# 連結かどうかの判定（answer = true のとき連結）
ans = True if all(visited) else False
if ans:
    print("The graph is connected.")
else:
    print("The graph is not connected.")
