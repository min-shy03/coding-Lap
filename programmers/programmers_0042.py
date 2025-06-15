# 최대공약수와 최소공배수

def solution(n, m):
    gcd = 0
    lcm = 0
    
    max_num, min_num = (n, m) if n > m else (m, n)
    
    # 두 정수가 같으면 최대공약수와 최대 공배수가 같다!
    if max_num == min_num :
        gcd = max_num
        lcm = min_num
        return [gcd, lcm]
        
    # 유클리드 호제법을 이용한 최대공약수 구하기
    while True :
        r = max_num % min_num
        if r == 0 :
            gcd = min_num
            break
        else :
            max_num = min_num            
            min_num = r

    # 두 정수 n과 m의 곱은 두 정수의 최대공약수와 최소공배수의 곱과 같다!
    lcm = (n * m) // gcd
    
    return [gcd,lcm]

print(solution(2,5))