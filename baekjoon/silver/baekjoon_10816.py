# 숫자 카드 2

n = int(input())
n_lst = map(int,input().split())
m = int(input())
m_lst = map(int,input().split())

d = {}
keys = d.keys()
for i in n_lst :
    if i in keys :
        d[i] += 1
    else :
        d[i] = 1

lst = []
for i in m_lst :
    if i in keys :
        lst.append(d[i])
    else :
        lst.append(0)

print(*lst)