# 素数判定
# 計算量：~O(sqrt(N))

def is_prime(N):
    if N == 1:
        return False
    LIMIT = int(N ** 0.5)
    for i in range(2, LIMIT + 1):
        if N % i == 0:
            return False
    return True
