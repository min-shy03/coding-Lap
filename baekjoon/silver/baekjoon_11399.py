# ATM

n = int(input())

lst = list(map(int, input().split()))

lst.sort()

total = []

# 누적합 알고리즘의 기본
for i in range(len(lst)) :
    if total :
        total.append(total[-1] + lst[i])
    else :
        total.append(lst[i])
    
print(sum(total))