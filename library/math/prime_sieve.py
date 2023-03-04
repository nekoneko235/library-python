# エラトステネスの篩
# 計算量：~O(N log(log(N)))

def sieve_of_Eratosthenes(N):
    primes = [True] * (N + 1)
    res = []

    # エラトステネスの篩
    LIMIT = int(N ** 0.5)
    for i in range(2, LIMIT + 1):
        if primes[i] is True:
            # x = 2i, 3i, 4i, ...と, N 以下の間ループし続ける
            for j in range(2 * i, N + 1, i):
                primes[j] = False

    # N 以下の素数を小さい順に res配列に追加
    for i in range(2, N + 1):
        if primes[i] is True:
            res.append(i)

    return res


arr = sieve_of_Eratosthenes(100)
print(arr)
