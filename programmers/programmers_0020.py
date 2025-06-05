# 등수 매기기

def solution(score):
    avg_score = []
    
    for s in score :
        avg_score.append(sum(s))
        
    ranking = sorted(avg_score, reverse=True)
    
    rank = 0
    skip = 0
    
    answer = [0] * len(avg_score)
    
    while ranking :
        if ranking.count(ranking[0]) > 1 :
            if skip :
                rank += skip
                skip = 0
            else : 
                rank += 1
            skip = ranking.count(ranking[0])
            for i in range(ranking.count(ranking[0])) :
                answer[avg_score.index(ranking[0])] = rank
                avg_score[avg_score.index(ranking[0])] = 0
                del ranking[0]
        else : 
            if skip :
                rank += skip
                skip = 0
            else : 
                rank += 1
                
            for i in range(ranking.count(ranking[0])) :
                answer[avg_score.index(ranking[0])] = rank
                avg_score[avg_score.index(ranking[0])] = 0
                del ranking[0]

    return answer

print(solution([[1, 3], [3, 1], [2, 3], [3, 2], [1, 2], [1, 1]])) 

# 더 간결하고 깔끔하게 짤 수 있다. 
# index() 함수는 무조건 앞의 위치한 값만 불러오는 점을 이용해서 등수가 중복되어도 처리가 가능하다.
# 여러 함수의 사용법을 숙지하자.

def solution(score):
    avg_score = []
    
    for s in score :
        avg_score.append(sum(s))
        
    ranking = sorted(avg_score, reverse=True)
    
    return [ranking.index(sum(i)) + 1 for i in score]

print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))
    