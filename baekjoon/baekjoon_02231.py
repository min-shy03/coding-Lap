# 2231번 분해합

n = int(input())

flag = True
for i in range(n) :
    total = 0
    for j in str(i) :
        total += int(j)
    
    if total + i == n :
        flag = False
        break

if flag :
    print(0)
else :
    print(i)