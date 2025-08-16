# 최솟값 찾기

from collections import deque

n, l = map(int, input().split())

lst = list(map(int, input().split()))

window = deque()

d = []

# 새로운 값이 들어올때마다 정렬하지 않고 현재 수보다 큰 값을 덱에서 없애서 시간 복잡도를 줄임
for i in range(n) :
    while window and window[-1][1] > lst[i] :
        window.pop()
    window.append([i,lst[i]])

    # 슬라이딩 윈도우 범위를 벗어나는 값은 제거하고 남은 값 중 가장 앞에 있는 값이 최솟값임
    while window and window[0][0] < (i - l) + 1 :
        window.popleft()

    d.append(window[0][1])

print(*d)