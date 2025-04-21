# 삼각형 외우기

a = int(input())
b = int(input())
c = int(input())

# 각도의 총합
total = a + b + c

# 각도의 합이 180도가 아니면 에러
if total != 180 :
    msg = "Error"
    
# 그 밑으론 삼각형의 종류 판별
elif a == b == c :
    msg = "Equilateral"
elif a == b or a == c or b == c :
    msg = "Isosceles"
else :
    msg = "Scalene"
    
print(msg)