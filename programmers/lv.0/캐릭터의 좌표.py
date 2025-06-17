# 캐릭터의 좌표

def solution(keyinput, board):
    answer = [0,0]

    board_boundary_1 = [board[0]//2, board[1]//2]
    board_boundary_2 = [-(board[0]//2), -(board[1]//2)]
    
    for char in keyinput :
        if char == "left" :
            if answer[0] > board_boundary_2[0] :
                answer[0] -= 1
        elif char == "right" :
            if answer[0] < board_boundary_1[0] :
                answer[0] += 1
        elif char == "up" :
            if answer[1] < board_boundary_1[1] :
                answer[1] += 1
        elif char == "down" :
            if answer[1] > board_boundary_2[1] :
                answer[1] -= 1
                
    return answer

print(solution(["left", "left", "up", "right", "right"],[11, 11]))