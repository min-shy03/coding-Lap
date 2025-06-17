# 이진수 더하기

def solution(bin1, bin2):
    # bin() 함수는 괄호 안에 10진수를 입력하면 2진수로 변환해준다.
    return bin(int(bin1,2) + int(bin2,2))[2:]

print(solution("10","11"))