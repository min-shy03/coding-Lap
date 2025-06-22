# 수 정렬하기 2
import sys

# input 함수 대신 input보다 실행이 빠른 readline 함수 사용
n = int(sys.stdin.readline().strip())

d = {}
keys = d.keys()
for _ in range(n) :
    num = int(sys.stdin.readline().strip())
    if num in keys :
        d[num] += 1
    else :
        d[num] = 1    

keys = sorted(d.keys())

for k in keys :
    for _ in range(d[k]) :
        print(k)