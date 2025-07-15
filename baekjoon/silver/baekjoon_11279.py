# 최대 힙

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
            # 힙의 가장 최솟값(음수로 들어있기 때문에 가장 최솟값이 곧 최댓값)
            print(-heapq.heappop(lst))
        else :
            print(0)
    else :
        # lst 힙에 x 원소 음수로 추가 (힙에서 pop은 최솟값을 뽑기 때문에 음수로 넣은 후 pop하기 위함)
        heapq.heappush(lst, -x)