# 수열

n = int(input())

total = 0
for i in range(1, n+1) :
    
    # i가 약수로 등장하는 횟수를 구하기
    total += i * (n // i)
    
print(total)