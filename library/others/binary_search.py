import time

# 二分探索（Lower-Bound）
# 計算量：O(logN)
# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_a


def binary_search(arr, key):
    left = -1
    right = len(arr)

    while abs(right - left) > 1:
        mid = (left + right) // 2
        if arr[mid] >= key:
            right = mid
        else:
            left = mid

    # 条件を満たす要素が存在しない場合は -1 を返却
    if right == len(arr) or arr[right] != key:
        return -1

    return right


def simple_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    # 条件を満たす要素が存在しない場合は -1 を返却
    return -1


# 1から10^12までの整数の配列を生成
arr = []
for i in range(1, 10**8 + 1):
    arr.append(i)

# 当然だが、二分探索の方が高速
time_start = time.time()
print(simple_search(arr, 0))
time_end = time.time()
print(f"Time: {time_end - time_start:.3f} sec")

time_start = time.time()
print(binary_search(arr, 0))
time_end = time.time()
print(f"Time: {time_end - time_start:.3f} sec")
