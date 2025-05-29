# 숨어있는 숫자의 덧셈 (2)

def solution(my_string):
    answer = 0
    
    digit = ""
    for char in my_string :
        if char.isdigit() :
            digit += char
        else :
            if digit :
                answer += int(digit)
            digit = ""
    
    if digit :
        answer += int(digit)
    
    return answer 

print(solution("aAb1B2cC34oOp")) 