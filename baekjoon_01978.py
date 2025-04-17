# 소수 찾기

# 주어진 N개의 수 중 소수가 몇 개인지 출력하라
# 소수 : 약수가 자기 자신과 1밖에 없는 수

count = int(input())

num_lst = list(map(int,input().split()))

prime = 0

for i in num_lst :
    # 이 코드에서 리스트를 생성 할 필요 없이 17번 if문이 실행된다면 그 수는 소수가 아님을 판명할 수 있다 
    # 다시 말해 코드 개선 여지가 있다.
    # 이 알고리즘을 잘 생각해보자.
    lst = []
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            lst.append(j)
            if j != (i // j):
                lst.append(i // j)
    
    if len(lst) == 2 :
        prime+=1
        
print(prime)