# 분수 합

# a, b의 최대 공약수 구하는 함수
def gcd(a, b) :
    while b :
        a , b = b , a % b
    
    return a


a, b = map(int, input().split())
c, d = map(int, input().split())

# 두 분모의 최대공약수
g = gcd(b,d)

# 두 분모의 최대공배수 = 두 분모의 곱 나누기 최대공약수
lcm = (b * d) // g

# 통분 과정
a = (lcm // b) * a
c = (lcm // d) * c

# 기약 분수화
x = a + c

# 분자와 분모의 최대공약수로 나누기
g = gcd(x,lcm)

x = x // g 
lcm = lcm // g

print(x, lcm)