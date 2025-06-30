# 스택 수열

import sys

n = int(sys.stdin.readline().strip())

stack = []
i = 1
sign = []

for _ in range(n) :
    num = int(sys.stdin.readline().strip())
    
    while i <= num :
        stack.append(i)
        i += 1
        sign.append("+")
    
    if stack[-1] == num :
        stack.pop()
        sign.append("-")
    else :
        print("NO")
        quit()

for i in sign :
    print(i)