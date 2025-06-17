# 삼총사

def solution(number): 
    answer = 0
    
    while len(number) > 2 :
        x = number.pop(0)
        
        idx_1 = 0
        
        for count in range(len(number)-1, 0,-1) :
            idx_2 = 1
            for i in range(count) :
                if x + number[idx_1] + number[idx_1+idx_2] == 0 :
                    answer += 1 
                idx_2 += 1
            idx_1 += 1
            
    return answer

print(solution([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]))
