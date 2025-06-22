# 덩치

n = int(input())

lst = []
for _ in range(n) :
    lst.append(tuple(map(int, input().split())))
    
weight = [i[0] for i in lst]
height = [i[1] for i in lst]

lose_lst = [0] * n
for idx, val in enumerate(lst) :
    for i in range(n) :
        if val[0] < weight[i] and val[1] < height[i] :
            lose_lst[idx] += 1

# lose_lst = 1,1,0,1,4

for idx, val in enumerate(lose_lst) :
    lose_lst[idx] = val + 1
    
print(*lose_lst)