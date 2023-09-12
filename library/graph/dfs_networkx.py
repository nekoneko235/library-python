# 深さ優先探索 (NetworkX)
# 計算量：~O(N + M)

import networkx as nx

N, M = map(int, input().split())
G = nx.Graph()
G.add_nodes_from(range(1, N + 1))

for _ in range(M):
    A, B = map(int, input().split())
    G.add_edge(A, B)

ans = True if nx.is_connected(G) else False
if ans:
    print("The graph is connected.")
else:
    print("The graph is not connected.")

# 043 - Depth First Search
# https://atcoder.jp/contests/math-and-algorithm/submissions/45436670
# https://atcoder.jp/contests/math-and-algorithm/submissions/45436619
