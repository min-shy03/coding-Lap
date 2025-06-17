# 최소직사각형

def solution(sizes):
    # 각 명함중 큰 변과 작은 변 분리 
    big = [max(i) for i in sizes]
    small = [min(i) for i in sizes]
    
    # 큰 변 중 가장 큰 값과 작은 변중 가장 큰 값 곱
    return max(big) * max(small)

print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))