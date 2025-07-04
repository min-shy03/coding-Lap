# 베르트랑 공준

def prime(n, m) :
    # 최댓값까지 걸러줄 소수들만 뽑기 그 이상의 소수는 최댓값을 넘어감
    base_prime = [True] * (int(m ** 0.5)+1)
    base_prime[0] = base_prime[1] = False
    
    for i in range(2, int(m ** 0.5) + 1) :
        if base_prime[i] :
            for j in range(i * i, int(m ** 0.5) + 1, i) :
                base_prime[j] = False
    
    # n과 m 구간의 합성수를 걸러줄 소수 리스트
    base_prime_num = [i for i,v in enumerate(base_prime) if v]
    
    # 구간 수 만큼 리스트 생성
    num_lst = [True] * (m - n + 1)
    
    # 위에서 찾은 소수 리스트를 하나씩 받아옴
    for p in base_prime_num :
        # p의 배수 중 n 이상인 가장 작은 수를 시작 지점으로 삭제하기
        start = max(p * p, ((n + p -1) // p) * p)
        for z in range(start, m + 1, p) :
            # 인덱스 값은 0 부터 시작함으로 시작값 빼주기
            num_lst[z - n] = False
    
    # n이 1부터 시작할 경우 1은 소수가 아님으로 False 처리
    if n == 1 :
        num_lst[0] = False 
    
    # start=n => 인덱스를 어디서 부터 시작할 것인지 정하는 매개변수 기본값은 0
    return len([i for i,v in enumerate(num_lst, start=n) if v])

while True :
    n = int(input())
    
    if n == 0 :
        break
    else :
        # n보다 크거나 2n보다 작거나 같은 소수의 개수
        print(prime(n+1, 2 * n))