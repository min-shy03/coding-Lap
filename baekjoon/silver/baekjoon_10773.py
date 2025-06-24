# 제로
# 스택 자료구조 공부용

count = int(input())

lst = []
for _ in range(count) :
    n = int(input())
    
    if n != 0 :
        lst.append(n)
    else :
        lst.pop()

print(sum(lst))