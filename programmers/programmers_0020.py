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