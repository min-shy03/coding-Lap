# 모음 제거

def solution(my_string):
    return "".join([char for char in my_string if char not in "aeiou"])

print(solution("nice to meet you"))