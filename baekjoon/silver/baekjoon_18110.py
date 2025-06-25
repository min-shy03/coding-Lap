# solved.ac

from collections import deque
import sys

# 파이썬 내장함수로 구현된 round 함수는 0.5일때 제대로 동작을 안한다. 직접 만들어서 쓰자
def round(num) :
    if num - int(num) >= 0.5 :
        num = int(num) + 1
    else :
        num = int(num)
    
    return num

count = int(sys.stdin.readline().strip())
if count == 0 :
    print(0)
    quit()

del_person = (count * 0.15)

del_person = round(del_person)

q = deque()


for _ in range(count) :
    q.append(int(sys.stdin.readline().strip()))

# sorted한 queue를 다시 deque로 감싸서 queue 구조로 만들기
q = deque(sorted(q))

# count의 30% 인 del_person 만큼 앞 뒤로 제거
for _ in range(del_person) :
    q.popleft()
    q.pop()
    

print(round(sum(q) / len(q)))