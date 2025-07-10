# 2차원 배열의 합

# 누적 합과 구간 합을 이용한 문제. 복습 필요

import sys

n, m = map(int, input().split())

lst = []

for _ in range(n) :
    l = list(map(int, input().split()))
    
    lst.append(l)

total_lst = []
   
# 누적 합 구하기
for q in lst :
    total = [q[0]]
    
    for p in range(1, m) :
        total.append(total[p-1] + q[p])
    
    total_lst.append(total)
    
k = int(input())

# 구간 합 구하기
for _ in range(k) :
    i,j,x,y = map(int, input().split())
    
    t = 0
    for q in range(i-1, x) :
        if j == 1 :
            t += total_lst[q][y-1]
            continue
        else :
            t += total_lst[q][y-1] - total_lst[q][j-2]
    
    print(t)