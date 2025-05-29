# 안전 지대

# 2차원 배열로 된 보드 위에서 안전한 지역을 찾아라.
# 지뢰의 1칸 주변은 모두 위험지역이다.

# 알고리즘 작성
# 1. 지뢰의 위치를 찾는다. [1 위치 찾기]
# 2. 지뢰의 가로, 세로, 대각선을 1로 바꿔준다.
def solution(board):
    answer = 0
    
    # 처음 지뢰 위치 담을 리스트
    location_lst = []
    
    for row in range(len(board)) :
        for col in range(len(board)) :
            # 지뢰의 위치 담기
            if board[row][col] == 1 :
                location_lst.append((row,col))        
        
    
    # location에 담긴 위치를 기반으로 board내 주변 0 지역을 1로 바꾸기
    for loc in location_lst :
        up = down = left = right = loc_1 = loc_5 = loc_11 = loc_7 = False
        # 위쪽
        if loc[0]-1 >= 0 : 
            board[loc[0]-1][loc[1]] = 1 
            up = True
        # 아래쪽
        if loc[0]+1 < len(board) :
            board[loc[0]+1][loc[1]] = 1 
            down = True
        # 오른쪽
        if loc[1]+1 < len(board) :
            board[loc[0]][loc[1]+1] = 1
            right = True
        # 왼쪽
        if loc[1]-1 >= 0 :
            board[loc[0]][loc[1]-1] = 1
            left = True
        # 왼쪽 위 대각 11시 방향  
        if up and left :  
            board[loc[0]-1][loc[1]-1] = 1
        # 왼쪽 아래 대각 7시 방향
        if down and left :
            board[loc[0]+1][loc[1]-1] = 1
        # 오른쪽 위 대각 1시 방향
        if up and right :
            board[loc[0]-1][loc[1]+1] = 1
        # 오른쪽 아래 대각 5시 방향
        if down and right :
            board[loc[0]+1][loc[1]+1] = 1
    
    count = 0
    for row in range(len(board)) :
        for col in range(len(board)) :
            # 지뢰의 위치 담기
            if board[row][col] == 0 :
                count += 1 
    
    return count

print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))