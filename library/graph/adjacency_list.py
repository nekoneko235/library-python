# 隣接リスト

# 入力
n, v = map(int, input().split())

# 隣接リストの作成 (0-indexed)
G = [list() for _ in range(n)]  # G[i] は頂点 i に隣接する頂点のリスト
for i in range(v):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)  # 頂点 a に隣接する頂点として b を追加
    G[b].append(a)  # 頂点 b に隣接する頂点として a を追加

# 出力（len(G[i]) は頂点 i に隣接する頂点のリストの大きさ ＝ 次数）
for i in range(n):
    output = str(i) + ": {"
    for j in range(len(G[i])):
        if j >= 1:
            output += ","
        output += str(G[i][j])  # G[i][j] は頂点 i に隣接する頂点のうち j+1 番目のもの
    output += "}"
    print(output)
