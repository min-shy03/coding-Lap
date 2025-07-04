# 피보나치 함수

count = int(input())

for _ in range(count) :
    n = int(input())
    
    lst = [1,1]
    if n == 0 :
        lst = [1, 0]
    elif n == 1 :
        lst = [0, 1]
    else :
        for _ in range(2, n) :
            x = lst[1]
            lst[1] = lst[0] + lst[1]
            lst[0] = x
    
    print(*lst)