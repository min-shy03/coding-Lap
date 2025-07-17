# 구간 합 구하기 5

# DP 개념과 누적, 구간 합 개념을 이용하여 문제를 풀어보자
import sys

n, m = map(int, sys.stdin.readline().strip().split())

# 원본 리스트에 0 인덱스 위치 더 추가
A = [[0] * (n + 1)]

# (n+1) * (n+1) 사이즈의 누적 합 리스트 0으로 생성
D = [[0] * (n + 1) for _ in range(n + 1)]
 
for _ in range(n) :
    A_row = [0] + [int(x) for x in sys.stdin.readline().strip().split()]
    A.append(A_row)
    
# 누적 합 구하기
for i in range(1, n + 1) :
    for j in range(1, n + 1) :
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

for _ in range(m) :
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    
    print(result)