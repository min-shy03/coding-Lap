# 팩토리얼

def solution(n):
    i = 1
    answer = 1
    
    while True :
        answer *= i
        if answer > n :
            i -= 1
            break
        i += 1
    return i

print(solution(7))