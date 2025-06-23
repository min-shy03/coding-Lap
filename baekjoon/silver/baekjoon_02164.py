# 카드2

n = int(input())

lst = []
# 처음 카드 패 생성
for i in range(1,n+1) :
    if i % 2 == 0 :
        lst.append(i)

# n이 홀수면 맨 앞에 다시 붙여주기
if n % 2 :
    lst.insert(0, n)

# lst가 1이 될 때 까지 거름망
while len(lst) != 1 :
    x = 0
    if len(lst) % 2 :
        x = lst[-1]
    lst = [val for idx,val in enumerate(lst) if idx % 2]

    if x :
        lst.insert(0, x)

print(lst[0])