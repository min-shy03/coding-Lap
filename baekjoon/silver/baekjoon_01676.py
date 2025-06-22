# 팩토리얼 0의 개수
# 파이썬은 생각보다 큰 수의 계산을 빠르게 잘한다. 
# 메모리가 허용하는 한 시간 초과는 걱정할 필요는 잘 없다.

n = int(input())

total = 1

# n 값이 500이 들어와도 연산이 크게 느려지지 않는다!
for i in range(1, n+1) :
    total *= i
    
count = 0
for i in str(total)[::-1] :
    if i != "0" :  
        break
    
    count += 1
    
print(count)