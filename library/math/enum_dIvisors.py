# 約数列挙
# 計算量：~O(sqrt(N))

def enum_divisors(N):
    LIMIT = int(N ** 0.5)
    divisors = []
    for i in range(1, LIMIT + 1):
        if N % i == 0:
            divisors.append(i)
            if i != N // i:
                divisors.append(N // i)
    return divisors
