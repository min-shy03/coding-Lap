# 테스트 케이스 횟수
test_count = int(input())

for _ in range(test_count) :
    # 각 동전 갯수 리스트
    lst = [0,0,0,0]
    
    # 거스름돈 입력
    money = int(input())
    
    # 거스름돈이 0이 될때까지 반복
    while money != 0 :
        if money >= 25 :
            r, money = divmod(money, 25)
            lst[0] += r
        elif money >= 10 :
            r, money = divmod(money, 10)
            lst[1] += r
        elif money >= 5 :
            r, money = divmod(money, 5)
            lst[2] += r
        else : 
            r, money = divmod(money, 1)
            lst[3] += r
            
    # 리스트 출력
    print(*lst)


