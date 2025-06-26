# 프린터 큐

from collections import deque

count = int(input())

for _ in range(count) :
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    
    # 타겟의 위치 저장 변수
    target = m
    lst = []
    while q :
        # 현재 팝의 가장 앞이 가장 큰 값이면
        if q[0] == max(q) :
            # 타겟이 나올 시간이면 브뤡
            if target == 0 :
                break
            else :
                target -= 1
            # 꺼내서 리스트에 담기 -> 이 행위는 count 변수 하나 만들어서 해도됨 불필요한 메모리 공간 차지
            lst.append(q.popleft())
        else :
            # 아닐 때 
            if target == 0 :
                target = len(q) - 1
            else : 
                target -= 1
            # 맨 뒤로 보냄
            q.rotate(-1)
    
    # 위에서 브렉 후 그 앞에 얼마나 출력이 돼있는지 확인 하는 용도
    print(len(lst)+1)