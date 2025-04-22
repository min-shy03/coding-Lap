# 직사각형에서 탈출하는 가장 빠른 루트를 찾아라.

# 코드 분석
# 이 문제에선 양수 이하의 수는 입력 되지 않기 때문에 절댓값을 쓸 이유가 없다.
# 또한 리스트에 담을 필요 없이 각 값만 바로 min() 함수에 넣어서 출력하면 된다.

# 각 축 저장 (x, y) 가 현재 위치 (w,h) 탈출 해야할 거리
x,y,w,h = map(int,input().split())

# 절댓값을 사용해 최소 거리 찾기
lst = []
lst.append(abs(x))
lst.append(abs(y))
lst.append(abs(w-x))
lst.append(abs(y-h))

print(min(lst))