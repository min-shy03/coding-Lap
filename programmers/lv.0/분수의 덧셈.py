# 분수의 덧셈

def solution(numer1, denom1, numer2, denom2):
    # 기약 분수 : 더이상 나눠지지 않는 분수
    
    # 통분 시 분모 - denom1로도 나눠지고 denom2로도 나눠지는 가장 작은 수
    # 최소공배수를 구해야함. 
    num = 1

    while True :        
        # 두개의 분모를 통분 시키기 위해 최소 공배수 구하기
        if num % denom1 == 0 and num % denom2 == 0 : 
            break
        else : 
            num += 1
            
    # 각 분자에 통분해서 더하기
    total = numer1 * (num // denom1) + numer2 * (num // denom2)
    
    # total = 현재 통분 된 분자
    # num   = 현재 통분 된 분모

    # 유클리드 호제법으로 최대공약수 찾아 기약분수화 조지기
    # 1. 큰 수와 작은 수 찾기
    maximum = total
    minimum = num

    if num > maximum :
        maximum, minimum = num, total
    

    # 2. 큰 수에서 작은 수 나눠 나머지가 찾은 후 나머지가 0이 될 때까지 큰 수 % 작은 수 반복
    #   -> 다음 계산에서는 전의 작은 수 였던 수가 큰 수가 되고 나머지가 작은 수가 된다.
    while True :
        remain = maximum % minimum
        # 나머지가 0이 되면 나눈 수가 최대 공약 수
        if remain == 0 :
            gcd = minimum
            break
        # 아니면 전의 작은 수를 큰수로 바꾸고 나머지를 작은 수로 
        else :
            maximum = minimum
            minimum = remain
    
    # 최대 공약수만큼 분자, 분모 나눠서 기약분수 만들기
    total //= gcd
    num //= gcd


    # total = 통분해 더한 분수값 , num = 통분한 분모값
    answer = [total, num]
    return answer

# 결과 확인
print(solution(3,8,3,8))