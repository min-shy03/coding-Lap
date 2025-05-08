# 모음 없애기

def solution(my_string):
    return "".join([char for char in my_string if char not in "aeiou"])

print(solution("nice to meet you"))