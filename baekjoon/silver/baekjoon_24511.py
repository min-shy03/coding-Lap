# queuestack

from collections import deque

n = int(input())
# 스택과 큐로 구분 돼 입력받을 줄 => 스택은 무시해도됨 들어오자마자 다시 그대로 나감
lst = list(map(int, input().split()))
# 각 스택과 큐에 들어갈 숫자들 => 위 lst와 동일한 인덱스 숫자는 없애도 됨
basic_num = list(map(int, input().split()))

# 오직 q만 있는 리스트
only_queue_lst = deque()

# 스택 거르기
for i in range(n) :
    if lst[i] == 0 :
        only_queue_lst.append(basic_num[i])

m = int(input())
input_num_lst = list(map(int, input().split()))

answer = []
for i in input_num_lst :
    only_queue_lst.appendleft(i)
    answer.append(only_queue_lst.pop())
    
print(*answer)