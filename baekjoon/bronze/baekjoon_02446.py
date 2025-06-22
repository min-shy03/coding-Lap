# 별 찍기 9번 문제

n = int(input())

space_count = 0

flag = True

for _ in range(2 * n - 1) :
    print(" " * space_count, end="")
    print("*" * (2 * n - 1))
    
    if n == 1 :
        flag = False
        
    if flag :
        n -= 1
        space_count += 1
    else :
        space_count -= 1
        n += 1