def solution(polynomial):
    answer = ''

    lst = list(polynomial.split())
    
    x_lst = [i for i in lst if "x" in i]
    int_lst = [int(i) for i in lst if i.isdigit()]
    
    x_total = 0
    for val in x_lst :
        if val == "x" :
            count = 1
        else :    
            count = int(val.replace("x", ""))
        
        x_total += count
    
    int_total = sum(int_lst)
    
    if int_total == 0 :
        int_lst = []
    
    if x_total and int_lst :
        if x_total == 1 :
            answer = f"x + {int_total}"    
        else :
            answer = f"{x_total}x + {int_total}"
    elif x_total and (not int_lst) :
        if x_total == 1 :
            answer = "x"
        else :
            answer = f"{x_total}x"
    else : 
        answer = f"{int_total}"
    
    return answer

print(solution("x"))