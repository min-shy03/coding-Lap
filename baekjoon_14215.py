# a, b, c가 주어졌을 때, 만들 수 있는 가장 큰 둘레를 구하는 프로그램을 작성하시오. 

a, b, c = map(int, input().split())

# 최댓값 찾기
max_num = a
    
if max_num < b :
    max_num = b
    
if max_num < c :
    max_num = c
    
# 다른 두 변의 합 찾기   
other = (a + b + c) - max_num

# 성립이 안되면 최댓값을 성립이 되도록 줄이기
if max_num >= other :
    # 최댓값을 다른 두 변의 합보다 1보다만 작게 만들어서 성립하도록 만들기
    max_num = other - 1

print(max_num + other)
