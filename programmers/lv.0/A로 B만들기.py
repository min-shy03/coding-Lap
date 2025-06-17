# A로 B 만들기

def solution(before, after):
    before = sorted(before)
    after = sorted(after)
    
    return 1 if before == after else 0

print(solution("olleh","hello"))