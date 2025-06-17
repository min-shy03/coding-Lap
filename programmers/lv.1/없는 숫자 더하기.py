# 없는 숫자 더하기

def solution(numbers):
    return sum([i for i in range(10) if i not in numbers])

print(solution([5,8,4,0,6,7,9]))