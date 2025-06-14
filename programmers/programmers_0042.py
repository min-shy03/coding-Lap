# 최대공약수와 최대 공배수

def solution(n, m):
    gcd = 0
    lcm = 0
    
    max_num, min_num = (n, m) if n > m else (m, n)
    
    if max_num == min_num :
        gcd = max_num
        lcm = min_num
        
    while True :
        r = max_num % min_num
        if r == 0 :
            gcd = min_num
            break
        else :
            max_num = min_num            
            min_num = r

    lcm = (n * m) // gcd
    
    return [gcd,lcm]

print(solution(2,5))