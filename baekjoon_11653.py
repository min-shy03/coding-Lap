# 소인수 분해
# 정수 n 을 소인수 분해하여 출력하라

# 이 코드는 내 힘으로 직접 짠게 아님으로 공부 및 코드 분석 제대로 필요
# 더욱 더 간결하게 코드를 구현할 수도 있음 힌트 : 루트 n 까지 반복

n = int(input())

count = 2

# 1은 소수도 합성수도 아니니 수킵
if n == 1 :
    quit()

# 나누는 수가 몫보다 높아지면 종료
while count <= n : 
    # 딱 나누어질 때까지 count 만큼 나눔
    if n % count == 0 :
        print(count)
        n //= count
        
    # 안 나누어 떨어지면 count 1 늘리기
    else :
        count += 1
