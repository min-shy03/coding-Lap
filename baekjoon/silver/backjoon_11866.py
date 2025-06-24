# 요세푸스 문제 0
from collections import deque

n, k = map(int, input().split())

lst = [i for i in range(1, n+1)]

q = deque()

start = k
for i in range(start-1, len(lst), k) :
    q.append(lst.pop(i))
    
print(q)