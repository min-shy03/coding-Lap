# 회의실 배정

import sys

n = int(sys.stdin.readline().strip())

lst = []

for _ in range(n) :
    lst.append(tuple(map(int,sys.stdin.readline().strip().split())))

# 가장 이른 시간에 끝나는 회의를 기준으로 정렬
lst.sort(key=lambda x : (x[1]))

# 가장 처음에 넣기
table = [lst[0]]
del lst[0]

for i in lst :
    # 가장 마지막에 열린 회의에서 가장 빨리 열리는 회의 순으로 넣기
    if table[-1][1] <= i[0] :
        table.append(i) 

print(len(table))