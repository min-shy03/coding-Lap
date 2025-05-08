# 입력받은 n 값 이하의 합성수를 모두 구하라.

def solution(n):
    answer = 0
    
    # 0,1,2 싹다 합성수가 될 수가 없음으로 3부터 시작
    for i in range(3,n+1) :
        # 2 이상의 짝수는 당연히 합성수
        if i % 2 == 0 :
            answer += 1
        else :
            # 홀수 중 인수를 가졌는지 판별
            for k in range(2,int(i ** 0.5) + 1) :
                if i % k == 0 :
                    answer += 1
                    break
            
    return answer