# 별 찍기 8번 문제

n = int(input())

block_count = 1
space_count = n - 1 

flag = True

for _ in range((2 * n - 1)) :    
    print("*" * block_count, end="")
    print(" " * (2 * space_count), end="")
    print("*" * block_count, )
    
    if block_count == n :
        flag = False
    
    if flag :
        block_count += 1
        space_count -= 1
    else :
        block_count -= 1
        space_count += 1  