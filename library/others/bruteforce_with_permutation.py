# 順列全探索
# 計算量：~O(N!)

import itertools

n = int(input())
arr = range(n)  # 0からn-1までのリスト
p_arr = itertools.permutations(arr)  # 全ての場合のリストを生成

for one_case in p_arr:
    for num in one_case:
        print(num, end=" ")
    print()
