# 오큰수
# 단조 감소 스택 공부해서 다시 풀어보기 지금은 매우 비효율적

from collections import deque

n = int(input())
lst = deque(map(int, input().split()))
stack = []
answer = []

for i in range(n) :
    stack.append([lst.popleft(), i])
    if i == n-1 :
        break
    
    while stack :
        if stack[-1][0] < lst[0] :
            stack[-1][0] = lst[0]
            answer.append(stack.pop())
        else :
            break
 
for i in range(len(stack)) :
    stack[i][0] = -1

answer = answer + stack
answer = sorted(answer, key=lambda x : x[1])
answer = [i[0] for i in answer]

print(*answer)

# ================================================
# 재풀이 코드

n = int(input())
lst = list(map(int, input().split()))


stack = []

answer = [0] * n

for i,v in enumerate(lst) :
    if not stack or stack[-1][1] > v :
        stack.append((i,v))
    else :
        while stack and stack[-1][1] < v :
            answer[stack[-1][0]] = v
            stack.pop()
            
        stack.append((i,v))

for i in stack :
    answer[i[0]] = -1

print(*answer)