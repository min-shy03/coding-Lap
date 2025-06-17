# 약수의 개수와 덧셈

def solution(left, right):
    answer = 0
    for i in range(left, right+1) :
        s = set()
        for k in range(1, int(i ** 0.5)+1) :
            if i % k == 0 :
                s.add(k)
                s.add(i//k)
        if len(s) % 2 :
            answer -= i
        else :
            answer += i
            
    return answer

print(solution(24,27))