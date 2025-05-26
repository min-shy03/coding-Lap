# 직사각형의 넓이 구하기

# 네 꼭짓점의 좌표가 담긴 리스트를 받아 직사각형의 넓이를 구해라

def solution(dots):
    answer = list(zip(*dots))
    answer = abs(max(answer[0]) - min(answer[0])) * abs(max(answer[1]) - min(answer[1]))
    return answer

print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))