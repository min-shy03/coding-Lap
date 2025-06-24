# 스택
import sys

count = int(sys.stdin.readline().strip())

lst = []
for _ in range(count) :
    command_lst = sys.stdin.readline().strip().split()
    
    command = command_lst[0] 
    # push x 처리
    if len(command_lst) > 1 :
        num = int(command_lst[1])
        
    if command == "push" :
        lst.append(num)
    elif command == "pop" :
        if lst :
            print(lst.pop())
        else :
            print("-1")
    elif command == "size" :
        print(len(lst))
    elif command == "empty" :
        if lst :
            print("0")
        else :
            print("1")
    elif command == "top" :
        if lst :
            print(lst[-1])
        else :
            print("-1")