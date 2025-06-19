# [1차] 비밀 지도
# 비트 연산자 개념 숙지 필요

def solution(n, arr1, arr2):
    answer = []
    arr1_bin = []
    arr2_bin = []
    for i in arr1 :
        arr1_bin.append("0" * (n - len(format(i, "b"))) + format(i,"b"))
        
    for i in arr2 :
        arr2_bin.append("0" * (n - len(format(i, "b"))) + format(i,"b")) 
    
    for j in range(n) :
        word = ""
        for k in range(n) :
            if arr1_bin[j][k] == "1" or arr2_bin[j][k] == "1" :
                word += "#"
            else :
                word += " "
        answer.append(word)
        
    return answer

print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))