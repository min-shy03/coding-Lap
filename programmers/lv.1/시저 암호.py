# 시저 암호

def solution(s, n):
    answer = ''
    
    alpha = {}
    
    for i in range(65,91) :
        alpha[chr(i)] = i
    
    for i in range(97,123) :
        alpha[chr(i)] = i
    
    for i in s :
        # 공백이면 스킵
        if i == " " :
            answer += " "
        # 대문자일 경우
        elif i.isupper() :
            if alpha[i] + n < 91 :
                answer += chr(alpha[i] + n)
            else : 
                answer += chr(65 + (((alpha[i] + n)) - 91))
        # 소문자일 경우
        else : 
            if alpha[i] + n < 123 :
                answer += chr(alpha[i] + n)
            else : 
                answer += chr(97 + (((alpha[i] + n)) - 123))
        
    return answer

print(solution("Z",1))