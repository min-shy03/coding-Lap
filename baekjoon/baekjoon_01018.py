# 체스판 다시 칠하기
n, m = map(int, input().split())

# 원래 코드
lst = []
for _ in range(n) :
    lst.append(input())

count_lst = []
for sero in range(n-7) :
    for garo in range(m-7) : # 여기까지 맨 윗 기준점 
        W_start_count = 0
        B_start_count = 0
        # W가 시작점일때의 기준
        W_start = {0 : "W", 1 : "B"}
        
        # B가 시작점일때의 기준
        B_start = {0 : "B", 1 : "W"}
        
        for i in range(8) :
            for j in range(8) :
                # 현재 위치
                now = lst[sero+i][garo+j]
                if W_start[j % 2] != now :
                    W_start_count +=1
                if B_start[j % 2] != now :
                    B_start_count +=1

            W_start, B_start = B_start, W_start
        
        count = W_start_count if W_start_count < B_start_count else B_start_count
        count_lst.append(count)  
        
print(min(count_lst))