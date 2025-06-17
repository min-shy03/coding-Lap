# 이상한 문자 만들기

def solution(s):
    s = list(s)
    i = 0
    for idx, val in enumerate(s) :
        if val != " " :
            if i % 2 :
                s[idx] = val.lower()
            else :
                s[idx] = val.upper()
            i += 1
        else : 
            i = 0
            
    return "".join(s)

print(solution("try  hello world "))