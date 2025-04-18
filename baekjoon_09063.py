# 내가 가질 땅의 면적은?
count = int(input())

# x,y 좌표값 저장할 리스트
x_lst = []
y_lst = []

# 좌표값 저장
for _ in range(count) :
    x, y = map(int,input().split())
    
    x_lst.append(x)
    y_lst.append(y)

# x,y의 최댓값 - x,y의 최솟값을 빼 가질 수 있는 절댓값 거리를 구한다.
x = max(x_lst) - min(x_lst)
y = max(y_lst) - min(y_lst)

# 면적 계산
square = x * y

print(square)
