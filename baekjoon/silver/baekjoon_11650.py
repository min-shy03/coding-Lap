# 좌표 정렬하기

n = int(input())

lst = []
for _ in range(n) :
    x = tuple(map(int, input().split()))
    lst.append(x)
    
lst = sorted(lst, key=lambda x: (x[0], x[1]))

for i in lst :
    print(*i)
