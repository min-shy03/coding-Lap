# 연속된 수의 합

def solution(num, total):
    answer = []
    avg = total / num
    dis = num / 2  
        
    if dis.is_integer() :
        val = int(avg) - (int(dis) - 1)
    else : 
        val = int(avg) - int(dis)
    
    for i in range(num) :
        answer.append(val)
        val += 1
        
    return answer

print(solution(5,15))