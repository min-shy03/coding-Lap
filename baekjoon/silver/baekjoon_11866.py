# 요세푸스 문제 0

# 챗지피티 답보고 풀었음.
# 큐 자료구조 및 메서드 활용법 제대로 익혀서 공부하기

from collections import deque

n, k = map(int, input().split())

q = deque(range(1,n+1))
lst = []

# 
while q :
    # rotate(x) : 큐의 원소를 오른쪽으로 x 만큼 회전 시키는 함수 앞에 -로 덮을 시 왼쪽으로 x 만큼 회전
    q.rotate(-(k-1))
    # 가장 앞 원소 pop 하는 함수
    lst.append(q.popleft())

print(f"<{", ".join(map(str, lst))}>")