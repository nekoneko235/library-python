# 幅優先探索
# 計算量：~O(N + M)

from collections import deque

# 入力
n, m = map(int, input().split())

# 隣接リストの作成
# 0-indexed
G = [list() for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

# 幅優先探索の初期化 (dist[i] = -1 のとき、未到達の白色頂点である）
dist = [-1] * n
Q = deque([])
dist[0] = 0
Q.append(0) # Q に 0 を追加（操作 1）

# 幅優先探索
while len(Q) >= 1:
    pos = Q.popleft() # Q の先頭を調べ、これを取り出す（操作 2, 3）
    for nex in G[pos]:
        if dist[nex] == -1:
            dist[nex] = dist[pos] + 1
            Q.append(nex) # Q に nex を追加（操作 1）

# 頂点 1 から各頂点までの最短距離を出力
for i in range(n):
    print(dist[i])
