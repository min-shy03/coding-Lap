# 공원 산책 문제

def solution(park, routes):
    answer = []
    
    # 공원 가로 길이
    park_width = len(park[0]) - 1
    # 공원 세로 길이
    park_length = len(park) - 1
    
    # 시작 위치 찾기
    start = [0,0]
    for idx,val in enumerate(park) :
        if "S" in val :
            start[0] = idx 
            for i,v in enumerate(val) :
                if v == "S" :
                    start[1] = i
                    break
    
    for char in routes :
        # 방향과 횟수 분리
        loc, count = char.split()
        
        # 진행 방향에 X가 있는지 확인하기 위한 불린 변수
        check = True
        
        count = int(count)
        if loc == "E" :
            # 현재 위치 + 이동 횟수가 공원의 전체 크기를 넘어가면 무시 밑의 코드를 실행하려면 무조건 통과해야됨
            if not start[1] + count <= park_width :
                continue
                
            # 현재 가로줄에서 끝까지 이동할때 까지 X가 없는지 체크하고 있으면 check = False 
            for i in range(start[1], start[1] + count+1) :
                if park[start[0]][i] == "X" :
                    check = False
                    break
            
            # 위 for문에서 check가 걸리지 않으면 그만큼 이동
            if check :
                start[1] += count
            
        elif loc == "W" :
            if not start[1] - count >= 0 :
                continue
            
            for i in range(start[1], start[1] - count - 1 , -1) :
                if park[start[0]][i] == "X" :
                    check = False
                    break
                
            if check :
                start[1] -= count
            
        elif loc == "S" :
            if not start[0] + count <= park_length :
                continue
            
            for i in range(start[0], start[0] + count+1) :
                if park[i][start[1]] == "X" :
                    check = False
                    break
                
            if check :
                start[0] += count
                
        else : 
            if not start[0] - count >= 0 :
                continue
            
            for i in range(start[0], start[0] - count - 1, -1) :
                if park[i][start[1]] == "X" :
                    check = False
                    break
            if check :
                start[0] -= count
    
    return start

print(solution(["OXO", "XSX", "OXO"],["S 1", "E 1", "W 1", "N 1"]))