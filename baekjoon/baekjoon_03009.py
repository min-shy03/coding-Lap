# 직사각형의 네 번째 점 구하기
# 각 x,y 좌표값 담는 리스트
x_lst = []
y_lst = []

# 리스트에 좌표값 담기
for _ in range(3) :
    x, y = map(int,input().split())
    
    x_lst.append(x)
    y_lst.append(y)

# x,y 값에서 한 번씩만 나온 좌표값이 직사각형을 완성할 때 필요한 x,y 좌표값임으로 그 값을 찾는다.
for i in range(3) :
    if x_lst.count(x_lst[i]) == 1 :
        x4 = x_lst[i]
    
    if y_lst.count(y_lst[i]) == 1 :
        y4 = y_lst[i]

print(x4,y4)