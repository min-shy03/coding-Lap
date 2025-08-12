# 잃어버린 괄호

from collections import deque

# 식
sick = input()

# 빼기 위치 리스트
minus = deque()

# 피연산자 리스트
operand = deque()

num = ""

# 수식에 - 존재하는지
flag = True

for idx, val in enumerate(sick) :
    if not val.isdigit() :
        if val == "-" :
            flag = False
            minus.append(idx)
        
        operand.append((int(num), idx-1))
        num = ""
    else :
        num += val
        
operand.append((int(num), idx))

# 빼기 뒤에 있는 숫자들을 다음 빼기가 나올 때 까지 다 더함
# 빼기가 하나 남았으면 뒤에 있는 숫자들 다 더해서 빼기

# 수식에 빼기가 하나도 없으면 총합이 답
if flag :
    print(sum([i[0] for i in operand]))
    quit()

m = minus.popleft()
total = 0

# 처음 마이너스가 나올때까지 토탈에 더해줌
while operand[0][1] < m :
    total += operand.popleft()[0]
    

# 빼야할 총량
total_minus = 0

while minus :
    if operand[0][1] > minus[0] :
        m = minus.popleft()
        total -= total_minus
        total_minus = 0
    
    total_minus += operand.popleft()[0]
    
# 마지막 빼기 뒤에 남은 연산자와 total 마이너스에 들어있는 값 더해서 빼기
total -= sum([i[0] for i in operand if i[1] > m]) + total_minus

print(total)