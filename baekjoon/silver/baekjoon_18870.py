# 좌표 압축

n = int(input())

# 1000 999 1000 999 1000 999
lst = list(map(int,input().split()))
# 2000만 번 돌음
s = sorted(set(lst))

d = {}

# 100만번 돌음
for idx,val in enumerate(s) :
    d[val] = idx

# 100만 번 돌음
for idx,val in enumerate(lst) :
    lst[idx] = d[val]
    
print(*lst)