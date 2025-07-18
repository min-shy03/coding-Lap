# 나머지 합

import math

n, m = map(int, input().split())

lst = list(map(int, input().split()))

A = [lst[0]]

# 누적 합 구하기
for i in range(1, n) :
    A.append(A[i-1] + lst[i])
    
# 합 배열을 m으로 나머지 배열 구하기
R = []

for i in A :
    R.append(i % m)

count = 0 

d = {}
key = d.keys()

for i in R :
    if i in key :
        d[i] += 1
    else :
        d[i] = 1

if 0 in key :
    count += d[0]

for i in d.items() :
    if i[1] > 1 :
        count += math.comb(i[1], 2)

print(count)