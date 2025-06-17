# 같은 숫자는 싫어

def solution(arr):
    answer = []
    
    for val in arr :
        if val not in answer or val != answer[-1] :
            answer.append(val)
    
    return answer

print(solution([4,4,4,3,3]))