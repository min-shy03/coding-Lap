# 음양 더하기

def solution(absolutes, signs):
    answer = 0
    for idx, val in enumerate(absolutes) :
        if signs[idx] :
            answer += val
        else :
            answer -= val
            
    return answer

print(solution([1,2,3],[False,False,True]))