# 나머지가 1이 되는 수 찾기

def solution(n):
    if n % 2 :
        return 2
    
    x = 3
    while True :
        if n % x == 1 :
            break
        x += 1
    
    return x

print(solution())