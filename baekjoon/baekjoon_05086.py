# 약수와 배수 판별

# a * b = n 이라고 할 때 a 와 b 는 n의 약수이다.
# n은 a와 b의 배수이다.

# n % a 혹은 n % b를 했을 때 나머지가 0이면 a 혹은 b는 n의 약수이다.
# n은 a,b의 배수이다.

while True:
    a, b = map(int,input().split())
    
    if a == 0 and b == 0 :
        break

    flag = "배수 판별"
    msg = ""
    
    if b > a :
        a , b = b, a
        flag = "약수 판별"
        
    if a % b == 0 :
        if flag == "배수 판별" :
            msg = "multiple"
        else :
            msg = "factor"
    else :
        msg = "neither"
    
    print(msg)

