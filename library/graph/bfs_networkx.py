# 幅優先探索
# 計算量：~O(N + M)

import networkx as nx

N, M = map(int, input().split())
G = nx.Graph()
G.add_nodes_from(range(1, N + 1))

for _ in range(M):
    A, B = map(int, input().split())
    G.add_edge(A, B)

length = nx.single_source_shortest_path_length(G, 1)

for i in range(1, N + 1):
    print(length.get(i, -1))

# 044 - Shortest Path 1
# https://atcoder.jp/contests/math-and-algorithm/submissions/45438576
# https://atcoder.jp/contests/math-and-algorithm/submissions/45438507
