# 집합
# 비트마스킹 공부해서 다시 풀기 잘못된 방식으로 풀음

import sys

n = int(sys.stdin.readline().strip())

s = set()

for _ in range(n) :
    command, *arg = sys.stdin.readline().strip().split()
    
    if arg :
        arg[0] = int(arg[0])
    
    if command == "add" :
        if arg[0] not in s :
            s.add(arg[0])
    elif command == "remove" :
        if arg[0] in s :
            s.remove(arg[0])
    elif command == "check" :
        if arg[0] in s :
            print("1")
        else :
            print("0")
    elif command == "toggle" :
        if arg[0] in s :
            s.remove(arg[0])
        else :
            s.add(arg[0])
    elif command == "all" :
        s = set(i for i in range(1,21))
    else :
        s = set()