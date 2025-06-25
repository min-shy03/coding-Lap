# 소수 구하기

# 에라토스테네스의 체를 기반으로 구간 소수 체 함수 구현

import math

def segmented_sieve(n, m):
    # 1. sqrt(m) 이하의 소수들을 먼저 구한다 (기본 체)
    limit = int(math.isqrt(m))
    is_prime_small = [True] * (limit + 1)
    is_prime_small[0] = is_prime_small[1] = False

    for i in range(2, limit + 1):
        if is_prime_small[i]:
            for j in range(i * i, limit + 1, i):
                is_prime_small[j] = False

    base_primes = [i for i, val in enumerate(is_prime_small) if val]

    # 2. [n, m] 구간에 대한 소수 여부 판별 리스트
    is_prime_range = [True] * (m - n + 1)

    for p in base_primes:
        # p의 배수 중 n 이상인 가장 작은 수부터 지움
        start = max(p * p, ((n + p - 1) // p) * p)
        for j in range(start, m + 1, p):
            is_prime_range[j - n] = False

    if n == 1:
        is_prime_range[0] = False

    # 3. 살아남은 수들만 소수로 반환
    return [i for i, val in enumerate(is_prime_range, start=n) if val]

n, m = map(int,input().split())

for i in segmented_sieve(n,m) :
    print(i)