# 다음에 올 숫자

def solution(common):
    dis1 = common[1] - common[0]
    dis2 = common[2] - common[1]
    
    if dis1 == 0 and dis2 == 0 :
        return common[-1]
    
    cd = 0
    cr = 0
    
    if dis2 // dis1 == 1 :
        cd = dis2
    else :
        cr = dis2 / dis1
    
    if common[-1] * cr >= 1 :
        answer = int(common[-1] * cr)
    else :
        answer = common[-1] * cr
        
    return common[-1] + cd if cd else answer 

print(solution([5, 5, 5] ))