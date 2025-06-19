# 명예의 전당 (1)

def solution(k, score):
    answer = []
    owner = []
    
    for i in score :
        if len(owner) < k :
            owner.append(i)
            owner = sorted(owner)
            answer.append(owner[0])
        elif i <= owner[0] :
            answer.append(owner[0])
        else :
            owner[0] = i
            owner = sorted(owner)
            answer.append(owner[0])
            
    return answer

print(solution(4,[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))