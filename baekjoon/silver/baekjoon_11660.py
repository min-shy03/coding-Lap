# 구간 합 구하기 5

import sys
input = sys.stdin.readline

n,m = map(int, input().split())

# 원본 리스트
A = [[0] * (n + 1)]

# 누적 합 리스트 틀
D = [[0] * (n + 1) for _ in range(n + 1)]

# 원본 리스트 추가
for _ in range(n) :
    A_row = [0] + list(map(int, input().split()))
    A.append(A_row)

# 누적 합 리스트 생성
for i in range(1, n+1) :
    for j in range(1, n+1) :
        D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + A[i][j]

# 구간 합 구하기
for _ in range(m) :
    x1, y1, x2, y2 = map(int,input().split())
    
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)