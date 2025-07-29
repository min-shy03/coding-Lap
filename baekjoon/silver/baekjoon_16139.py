# 인간 컴퓨터 상호작용

import sys
input = sys.stdin.readline

word = input().strip()

n = int(input().strip())

# 각 알파벳 숫자 리스트
alpha = {
    "a" : 0,
    "b" : 0,
    "c" : 0,
    "d" : 0,
    "e" : 0,
    "f" : 0,
    "g" : 0,
    "h" : 0,
    "i" : 0,
    "j" : 0,
    "k" : 0,
    "l" : 0,
    "m" : 0,
    "n" : 0,
    "o" : 0,
    "p" : 0,
    "q" : 0,
    "r" : 0,
    "s" : 0,
    "t" : 0,
    "u" : 0,
    "v" : 0,
    "w" : 0,
    "x" : 0,
    "y" : 0,
    "z" : 0
}

lst = []

# 딕셔너리 얇은 복사
for i in word :
    alpha[i] += 1
    lst.append(alpha.copy())

for _ in range(n) :
    a, b, c = input().strip().split()
    
    b = int(b)
    c = int(c)
    
    if b == 0 :
        print(lst[c][a])
    else :
        print(lst[c][a] - lst[b-1][a])