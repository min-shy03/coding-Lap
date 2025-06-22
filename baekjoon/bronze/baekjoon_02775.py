# 부녀회장이 될테야
count = int(input())

for i in range(count) :
    k = int(input())
    n = int(input())

    # 0층부터 시작하는 층 수별 호의 사람 리스트
    floor = [i for i in range(1,n+1)]
    
    # 층수 만큼 반복
    for _ in range(k) :
        lst = []
        # 호수 만큼 반복해서 새로운 리스트에 각 호수 인원 조건을 계속 합해줌
        for room in range(1, n+1) :
            lst.append(sum(floor[:room]))
        floor = lst 
        
    print(floor[-1])