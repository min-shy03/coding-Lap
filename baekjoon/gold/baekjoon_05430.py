# AC

from collections import deque

t = int(input())

for _ in range(t) :
    command = input()
    n = int(input())
    lst = input().split(",")
    
    lst[0] = lst[0].replace("[", "")
    lst[-1] = lst[-1].replace("]", "")
    
    if n == 0 :
        if "D" in command :
            print("error")
        else :
            print("[]")
        continue
    
    # 1 2 3 4
    lst = deque(list((map(int, lst))))
    # 4 3 2 1
    lst_reversed = deque(reversed(lst))
    
    # True = 원본 리스트 False = 역순
    current_lst = True
    
    for i in command :
        if i == "R" :
            current_lst = False if current_lst == True else True
        else : 
            if lst :
                if current_lst == False :
                    lst.pop()
                    lst_reversed.popleft()
                else :
                    lst.popleft()
                    lst_reversed.pop()
            else :
                print("error")
                break
    else :
        if current_lst :
            lst = list(map(str, lst))
            print(f"[{",".join(lst)}]")
        else :
            lst_reversed = list(map(str, lst_reversed))
            print(f"[{",".join(lst_reversed)}]")