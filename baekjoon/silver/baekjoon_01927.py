# 최소 힙

import heapq
import sys

n = int(sys.stdin.readline().strip())

lst = []
# 힙 생성
heapq.heapify(lst)

for _ in range(n) :
    x = int(sys.stdin.readline().strip())
    
    if x == 0 :
        if lst :
            # 힙의 가장 최솟값 pop
            print(heapq.heappop(lst))
        else :
            print(0)
    else :
        # lst 힙에 x 원소 추가
        heapq.heappush(lst, x)