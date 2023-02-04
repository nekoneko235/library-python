# 二分探索（Upper-Bound）
# 計算量：O(logN)
# bisect.bisect_right(A, K): Ai > K であるインデックスiのうち、
# 最小のものを返す。もし存在しない場合はlen(A)を返す

import bisect

# target array
#    0  1  2  3  4  5  6   7   8   9
A = [1, 4, 4, 7, 7, 8, 8, 11, 13, 19]
# target values
T = [4, 6, 7, 19, 20]

for t in T:
    ok = bisect.bisect_right(A, t)
    print(ok)
