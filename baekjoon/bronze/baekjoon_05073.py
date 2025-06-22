# 삼각형과 세 변

while True :
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0 :
        break

    # Invalid 구하기 위한 최댓값 찾기
    max_num = a
    
    if max_num < b :
        max_num = b
    
    if max_num < c :
        max_num = c
    
    # 나머지 두변의 합
    other = (a + b + c) - max_num
    
    if a == b == c :
        msg = "Equilateral"
    elif max_num >= other :
        msg = "Invalid"
    elif a == b or a == c or b == c :
        msg = "Isosceles"
    else :
        msg = "Scalene"
    
    print(msg)