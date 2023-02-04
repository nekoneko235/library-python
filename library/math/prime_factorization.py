# 素因数分解
# 計算量：~O(sqrt(N))

def prime_factorization(N):
    primes = []
    LIMIT = int(N ** 0.5)
    for i in range(2, LIMIT + 1):
        while N % i == 0:
            N /= i
            primes.append(i)
    # N が素数の場合
    if N >= 2:
        primes.append(int(N))
    return primes
