# 특이한 정렬

# 숫자가 담긴 리스트와 임의 정수 n 을 입력받아 n과 가까운 순서대로 정렬하라

def solution(numlist, n):
    answer = []
    
    if n not in numlist :
        numlist.append(n) 
    else :
        # n 값이 list 안에 있으면 그 값은 무조건 가장 처음으로 와야하기 때문에 넣고 시작
        answer.append(n)
    
    # 리스트를 오름차순으로 정렬
    numlist = sorted(numlist)
    
    # n 값을 기준으로 더 큰 리스트와 더 작은 리스트 분별
    small = numlist[:numlist.index(n)]
    big = numlist[numlist.index(n)+1:]
    
    # 더 작은 리스트, 더 큰 리스트
    while small and big  :
        # 절댓값이 같으면 큰 수부터 넣기
        if abs(small[-1] - n) == abs(big[0] - n) :
            answer.append(big.pop(0))
            answer.append(small.pop(-1))
        elif abs(small[-1] - n) > abs(big[0] - n) :
            answer.append(big.pop(0))
        else :
            answer.append(small.pop(-1))
    
    # 위 while 문이 끝나고 남은 리스트는 뒤에 더해주기
    if small :
        answer += small[::-1]
    else :
        answer += big
    
    return answer

print(solution([10000,20,36,47,40,6,10,7000], 30))