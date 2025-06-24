# 큐
# 가장 먼저 들어간 것이 가장 먼저나오는 구조


# 라이브러리 모듈로 불러와서 사용해야함
from collections import deque
import sys

count = int(sys.stdin.readline().strip())

# 리스트, 튜플, 셋 등과 같이 함수로 Create 가능
q = deque()

for _ in range(count) :
    # arg = push x 값 처리 위한 변수 값이 있을 수도 있고 없을 수도 있다
    command, *arg = sys.stdin.readline().strip().split()
    
    # 큐에 원소 추가
    if command == "push" :
        # 큐 원소 추가 방법
        q.append(int(arg[0]))
    # 큐의 가장 앞 원소 제거 및 빼오기
    elif command == "pop" :
        # 함수 뒤에 left가 붙은 것은 일부로 앞의 원소를 건드린다는 것을 표현하기 위함
        if q :
            print(q.popleft())
        else :
            print(-1)
    # 밑에 것들은 다 다른 컬렉션이랑 비슷한듯?
    elif command == "size" :
        print(len(q))
    elif command == "empty" :
        if q :
            print(0)
        else :
            print(1)
    elif command == "front" :
        if q :
            print(q[0])
        else :
            print(-1)
    elif command == "back" :
        if q :
            print(q[-1])
        else :
            print(-1)