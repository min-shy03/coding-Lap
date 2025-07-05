# 풍선 터뜨리기

from collections import deque

n = int(input())
num_lst = deque(list(map(int, input().split())))
q = deque([i for i in range(1, n+1)])
answer = []

for _ in range(n) :
    answer.append(q.popleft())
    num = num_lst.popleft()
    if num > 0 :
        num -= 1
    q.rotate(-num)
    num_lst.rotate(-num)
    
print(*answer)