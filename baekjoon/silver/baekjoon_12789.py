# 도키도키 간식드리미

from collections import deque

n = int(input())
line = deque(map(int, input().split()))
space = []
answer = [0]

while len(answer) - 1 < n :
    if line :
        if line[0] == answer[-1] + 1 :
            answer.append(line.popleft())
        else :
            if space :
                if space[-1] == answer[-1] + 1 : 
                    answer.append(space.pop())
                else :
                    space.append(line.popleft())
            else :
                space.append(line.popleft())
    elif space :
        if space[-1] == answer[-1] + 1 :
            answer.append(space.pop())
        else :
            print("Sad")
            quit()

print("Nice")