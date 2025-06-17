# 평행

# 모든 직선의 기울기를 구하여서 비교하기
# 수학적인 개념을 사용해서 더 줄일 수 있다 공부 후 다시 재풀이 필요

def solution(dots):
    line1 = set()
    
    x = []
    for _ in range(3) :
        
        a = dots.pop(0)
        
        for i in dots :
            x.append((i[1] - a[1]) / (i[0] - a[0]))
            
    return 1 if [i for i in x if x.count(i) == 2 or x.count(i) == 4 or x.count(i) == 6] else 0

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))