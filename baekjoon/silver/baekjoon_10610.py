# 30

# 30의 배수가 되기 위한 조건 매우 중요
# 1. 어떤 정수 n의 모든 자릿수의 합이 3의 배수이면 n은 3의 배수이다.
# 2. 끝자리에 0이 존재하면 그 수는 10의 배수이다.

n = input()

zero_flag = False

total = 0

for i in n :
    if i == "0" :
        zero_flag = True
    total += int(i)
    
if total % 3 == 0 and zero_flag :
    print("".join(sorted(list(n),reverse=True)))
else :
    print(-1)