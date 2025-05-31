# 외계어 사전

def solution(spell, dic):
    
    check = False
    # dic 단어 하나하나 받아오기
    for word in dic : 
        count = 0
        for alp in spell :
            if alp not in word :
                break
            count += 1
        if count == len(spell) :
            check = True
        
    
    return 1 if check else 2

print(solution(["p", "o", "s"],["sod", "eocd", "qixm", "adio", "soo"]))