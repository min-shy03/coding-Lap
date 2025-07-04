# 골드바흐 파티션

def prime(n) :
    lst = [True] * (n + 1)
    lst[0] = lst[1] = False
    
    for i in range(2, int(n ** 0.5) + 1) :
        if lst[i] :
            for j in range(i * i, n + 1 , i) :
                lst[j] = False

    return [i for i,v in enumerate(lst) if v]
    
count = int(input())

# 매 입력마다 체 돌릴수 없으니 가장 큰 값까지 미리 정해놓기
primes = prime(1000000)

for _ in range(count) :
    total = 0
    n = int(input())
    
    # 들어오는 n값보다 작은 소수들만 보고 판별하기
    n_under_lst = [i for i in primes if i < n]
    n_under_lst_set = set(n_under_lst)
    
    for i in n_under_lst :
        if i + i == n :
            total += 1
        elif n - i in n_under_lst_set :
            total += 1
            n_under_lst_set.remove(i)
            
    print(total)