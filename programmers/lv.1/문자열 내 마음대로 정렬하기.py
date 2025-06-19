# 문자열 내 마음대로 정렬하기

def solution(strings, n):
    n_lst = sorted(set([i[n] for i in strings]))
    str_lst = sorted(strings)
    answer = []
    
    for i in n_lst :
        for v in str_lst :
            if v[n] == i :
                answer.append(v)
    return answer


# 챗지피티 코드
def solution2(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))

print(solution(["abzcd","cdzab","abzfg","abzaa","abzbb","bbzaa"],2))
