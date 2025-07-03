# 구간 합 구하기 4

import sys

n, m = map(int, sys.stdin.readline().strip().split())

lst = list(map(int, sys.stdin.readline().strip().split()))

# 총 누적 합 구하기
total_lst = []
total_lst.append(lst[0])

for k in range(1, n) :
    total_lst.append(total_lst[k-1] + lst[k])

# 구간 합 구하기
for _ in range(m) :
    i, j = map(int, sys.stdin.readline().strip().split())
    
    # i가 1이면 처음부터임으로 그냥 누적합 출력
    if i == 1 :
        print(total_lst[j-1])
    # i 이전까지의 값을 빼고 나머지 누적합 출력
    else :
        print(total_lst[j-1] - total_lst[i-2])