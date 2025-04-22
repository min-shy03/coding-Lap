import math

a,b,v = map(int,input().split())

# 달팽이의 오름 규칙을 수식으로 표현
# math.ceil(x) = x보다 크거나 같은 가장 작은 정수를 반환하는 함수 
n = math.ceil((v - b) / (a - b))

print(n)
