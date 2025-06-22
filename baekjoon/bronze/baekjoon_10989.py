# 수 정렬하기 3
# sys 모듈 공부하기

import sys
input=sys.stdin.readline

count = int(input())

lst = [0] * 10000
for _ in range(count) :
    n = int(input())
    lst[n-1] += 1

for i in range(1,len(lst)+1) :
    for j in range(lst[i-1]) :
        print(i)