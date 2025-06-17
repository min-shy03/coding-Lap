# 종이 자르기

def solution(M, N):
    answer = (M-1) + ((N-1) * M)
    return answer

print(solution(2,2))