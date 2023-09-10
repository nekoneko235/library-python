# 深さ優先探索
# 計算量：~O(N + M)

from collections import deque

# 入力
N, M = map(int, input().split())

# 隣接リストの作成
# 0-indexed
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A - 1].append(B - 1)
    G[B - 1].append(A - 1)

# 深さ優先探索の初期化
visited = [False] * N
visited[0] = True
stack = deque([0])

# 深さ優先探索
while len(stack) > 0:
    pos = stack.pop()
    for next_pos in G[pos]:
        if not visited[next_pos]:
            visited[next_pos] = True
            stack.append(next_pos)

# 連結かどうかの判定（answer = true のとき連結）
ans = True if all(visited) else False
if ans:
    print("The graph is connected.")
else:
    print("The graph is not connected.")
