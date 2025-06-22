# 약수들의 합

while True :
    n= int(input())

    if n == -1 :
        break
    
    lst = []

    # n의 약수 찾아서 리스트에 담기 -> 백준 2501번과 연결된다!
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            lst.append(i)
            if i != n // i:
                lst.append(n // i)
                
    # 약수를 오름차순으로 정리!
    lst.sort()

    # 완전수 판별을 위해 자기 자신인 약수는 제외한다.
    del lst[-1]

    # 완전수 판별
    if sum(lst) == n :
        print(f"{n} =", end=" ")
        for i in lst :
            if i == lst[-1] :
                print(i)
                continue
            print(f"{i} + ", end="")
    else :
        print(f"{n} is NOT perfect.")
