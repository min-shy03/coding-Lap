# 삼총사

def solution(number): 
    lst = []
    
    while len(number) > 2 :
        x = number.pop(0)
        
        idx_1 = 0
        
        for count in range(len(number)-1, 0,-1) :
            idx_2 = 1
            for i in range(count) :
                lst.append((x,number[idx_1],number[idx_1+idx_2]))
                idx_2 += 1
            idx_1 += 1
            
    return len([i for i in lst if sum(i) == 0])

print(solution([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]))
