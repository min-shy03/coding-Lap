# 푸드 파이트 대회

def solution(food):
    # 물은 answer에 무조건 포함이기 때문에 미리 적고 시작
    answer = '0'
    # 가장 처음 원소는 물을 가리킴으로 없앰
    del food[0]
    
    # 가장 칼로리가 큰 음식부터 빼오기 위해 역순으로 바꿈
    food = food[::-1]
    
    count = len(food)
    for i in food :
        half = i // 2
        answer = (f"{count}" * half) + answer + (f"{count}" * half)
        count -= 1
    
    return answer

print(solution([1, 7, 1, 2]))