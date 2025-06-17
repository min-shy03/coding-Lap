# 삼각형의 완성조건(2)

def solution(sides):
    a = max(sides)
    b = min(sides)
    s = sum(sides)
    count = 0
    # case 1. 나머지 한 변의 길이가 가장 긴 변일 경우
    # a < X < s 를 만족하는 x의 갯수
    count += s - a - 1 
    
    # case 2. sides 리스트 에서의 최댓값이 가장 긴 변일 경우
    # a < b + x < s 를 만족하는 x 의갯수
    # 식 정리 하면 (a - b) < x < (s - b)
    count += (s - b) - (a - b) - 1
    
    return count + 1