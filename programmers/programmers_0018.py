# 유한소수 판별하기

def solution(a, b):
    maximum = max(a,b)
    minimum = min(a,b)
    
    # 기약분수를 구하기 위한 유클리드 호제법으로 최대 공약수 구하기
    while True :
        r = maximum % minimum
        if r == 0 :
            gcd = minimum
            break
        else :
            maximum = minimum
            minimum = r
    
    a = a // gcd
    b = b // gcd
    
    if b == 1 or b == 2 :
        return 1
    
    prime = 2 
    prime_lst = []
    while b >= prime : 
        if b % prime == 0 :
            b = b // prime
            prime_lst.append(prime)
        else :
            prime += 1
            
    s = set(prime_lst)
    if 2 in s :
        s.remove(2)
    if 5 in s :
        s.remove(5)
    
    return 2 if s else 1

print(solution(12,21))