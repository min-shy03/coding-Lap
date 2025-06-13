# 문자열 밀기

def solution(A, B):
    # a와 b가 같으면 즉시 0 반환 후 종료
    if A == B :
        return 0
    
    # 카운트
    answer = 0
    
    # 제자리로 돌아올 때까지 반복
    for i in range(len(A)) :
        answer += 1
        A = A[-1] + A[:-1]
        # 같아지면 그 즉시 종료 후 카운트 반환
        if A == B :
            return answer
    
    # 위에서 안끝났으면 평생 안같으니까 -1
    return -1

print(solution("abc","abc"))