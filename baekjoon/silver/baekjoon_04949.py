# 균형잡힌 세상

while True :
    flag = True
    char = input()
    
    if char == "." :
        break
    
    small_checker = []
    big_checker = [] 
    
    for idx,val in enumerate(char) :
        if val == "(" :
            small_checker.append(idx)
        elif val == "[" :
            big_checker.append(idx)
        elif val == ")" :
            if not small_checker :
                print("no")
                flag = False
                break
            else :
                if not big_checker :
                    del small_checker[-1]
                elif big_checker[-1] > small_checker[-1] :
                    flag = False
                    print("no")
                    break
                else :
                    del small_checker[-1]
        elif val == "]" :
            if not big_checker :
                flag = False
                print("no")
                break
            else :
                if not small_checker :
                    del big_checker[-1]
                elif small_checker[-1] > big_checker[-1] :
                    flag = False
                    print("no")
                    break
                else :
                    del big_checker[-1]

    if flag :
        if small_checker or big_checker :
            print("no")
            continue
        
        print("yes")         