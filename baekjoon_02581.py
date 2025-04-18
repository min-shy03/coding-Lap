# M~N 사이의 수 중 소수를 찾고 총합과 최솟값을 찾아라.

# 백준 1978번 소수찾기 문제 코드를 응용 가능

# 입력 받기
m = int(input())
n = int(input())

# 소수를 담을 리스트
prime_list = []

# m 부터 n까지 수 반복
for i in range(m, n+1) :
    # 0과 1 예외 처리
    if i < 2 :
        continue
    # 소수 판별 깃발
    is_prime = True
    
    # 소수 판별 반복문 0과 1은 생략한다. 어차피 0으로는 나눌 수 없고 1로 안나뉘는 수는 없기 때문
    for j in range(2, int(i ** 0.5) + 1):
        # 어떤 수에 나뉘는 수는 소수가 아님으로 바로 브렉 때려버리기 소수가 아님으로 판단
        if i % j == 0:
            is_prime = False
            break
    
    # 위 반복문에서 걸리지 않으면 그 수는 소수로 판단.
    if is_prime :
        prime_list.append(i)

# 출력
if len(prime_list) > 0 :
    print(sum(prime_list))
    print(min(prime_list))
else :
    print(-1)