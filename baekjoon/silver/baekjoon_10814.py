# 나이순 정렬

n = int(input())

lst = []
for i in range(n) :
    age, name = input().split()
    lst.append((i,int(age),name))

lst = sorted(lst, key=lambda x : (x[1], x[0]))

for i in lst :
    print(i[1],i[2])