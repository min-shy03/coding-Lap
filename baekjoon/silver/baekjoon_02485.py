# 가로수
# 문제 패턴 잘 파악하기

def gcd(a,b) :
    while b :
        a, b = b, a % b
        
    return a

n = int(input())

lst = []
for _ in range(n) :
    lst.append(int(input()))

# n 3일때
x = lst[-1] - lst[0]
a = lst[1] - lst[0]
b = lst[2] - lst[1]

if n > 3 :
    c = lst[3] - lst[2]
    g = gcd(gcd(a,b),c)
else :
    g = gcd(a,b)

print(x//g - (len(lst)-1))