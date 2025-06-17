# 가장 가까운 글자

def solution(s):
    answer = []
    alpha = {}
    
    for i in range(97,123) :
        alpha[chr(i)] = -1
    
    for idx,val in enumerate(s) :
        if alpha[val] != -1 :
            answer.append(idx - alpha[val])
            alpha[val] = idx
        else :
            answer.append(alpha[val])
            alpha[val] = idx
            
    return answer

print(solution("foobar"))