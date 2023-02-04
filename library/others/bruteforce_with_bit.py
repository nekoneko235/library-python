# bit全探索
# 計算量：~O(2^N x N)

arr = [1, 4, 10]
sum = 0

# 全ての選び方の数値の和の合計を計算
for bit in range(1<<len(arr)): # 0(0b000)から7(b111)まで
    for i in range(len(arr)):
        if bit & (1<<i): # 右からi番目にビットが立っているかどうか判定
            sum += arr[i]
print(sum) # 出力は60
