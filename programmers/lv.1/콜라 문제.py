# 콜라 문제

def solution(a, b, n):
    answer = 0
    
    while True :
        q, r = divmod(n, a)
        answer += q * b 
        n = (q * b) + r
        
        if n < a :
            break
        
    return answer

print(solution(4,2,20))