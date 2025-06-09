# 추억 점수

def solution(name, yearning, photo):
    # 각 인물 별 점수를 딕셔너리화
    score = dict(list(zip(name,yearning)))
    
    answer = []
    
    for i in photo :
        total = 0
        for j in i :
            if j in score :
                total += score[j]
        
        answer.append(total)
    
    return answer

print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))