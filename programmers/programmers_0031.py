# 자연수 뒤집어 배열로 만들기

def solution(n):
    n = list(str(n))
    n.reverse()
    return list(map(int,n))


print(solution(12345))