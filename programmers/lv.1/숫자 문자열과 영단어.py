# 숫자 문자열과 영단어 
# 코드 간단하고 더 좋은 방법으로 풀어보기

def solution(s):
    answer = ""
    d = {
        "zero" : "0",
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9"
    }
    
    word = ""
    for i in s :
        if i.isdigit() :
            answer += i
            continue
        
        word += i
        if word in d.keys() :
            answer += d[word]
            word = ""
            
    return int(answer)

print(solution("23four5six7"))