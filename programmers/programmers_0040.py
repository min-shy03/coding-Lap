# 평행

def solution(dots):
    
    line1 = set()
    
    # 발생할 수 있는 모든 직선 구하기
    x = []
    for _ in range(3) :
        a = dots.pop(0)
        for i in dots :
            x.append((i[1] - a[1]) / (i[0] - a[0]))
            
    return 1 if [i for i in x if x.count(i) == 2 or x.count(i) == 4 or x.count(i) == 6] else 0


print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))