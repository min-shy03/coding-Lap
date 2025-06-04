# 겹치는 선분의 길이

def solution(lines):
    # 주어진 선분들의 가장 양 끝 구하기
    x_point = []
    for i in lines :
        for j in i :
            x_point.append(j)
            
    max_x = max(x_point)
    min_x = min(x_point)
    
    # 각 선분 구간을 하나의 튜플로 지정하여 딕셔너리화 = count 재기 위함 ex) (0,1), (1,2), (2,3)...
    count = {}
    for i in range(min_x+1, max_x+1) :
        count[(i-1,i)] = 0
    
    # 각 주어진 선분들로 count 딕셔너리 각 구간을 1씩 더해줌
    for i in lines : 
        for j in range(i[0]+1,i[1]+1) :
            count[(j-1,j)] += 1
            
    return len([i for i in list(count.values()) if i > 1])

print(solution([[1,2],[2,3],[3,4]]))