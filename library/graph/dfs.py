# 深さ優先探索
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

# 深さ優先探索の初期化
visited = [False] * n
S = deque([]) # スタック S を定義
visited[0] = True
S.append(0) # S に 0 を追加

# 深さ優先探索
while len(S) >= 1:
    pos = S.pop() # S の一番上を調べ、これを取り出す
    for nex in G[pos]:
        if visited[nex] == False:
            visited[nex] = True
            S.append(nex) # S に nex を追加

# 連結かどうかの判定（answer = true のとき連結）
answer = True
for i in range(n):
    if visited[i] == False:
        answer = False
if answer == True:
    print("the graph is connected.")
else:
    print("The graph is not connected.")
