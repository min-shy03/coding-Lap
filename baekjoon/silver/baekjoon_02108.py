# 통계학

import sys

def round(n) :
    num = abs(n)
    if num - int(num) > 0.5 :
        num = int(num) + 1
    else :
        num = int(num)
        
    return num if n > 0 else num * -1

n = int(sys.stdin.readline().strip())


lst = []
d = {}
keys = d.keys()
for _ in range(n) :
    k = int(sys.stdin.readline().strip())
    lst.append(k)
    if k in keys :
        d[k] += 1
    else :
        d[k] = 1

# 산술평균 출력    
print(round(sum(lst)/n))

# 중앙값 출력
s = sorted(lst)
print(s[int(n/2)])

# 최빈 값 출력
m = max(list(d.values()))
mode = sorted([idx for idx,val in d.items() if val == m])
if len(mode) > 1 :    
    print(mode[1])
else :
    print(mode[0])

# 범위
if len(s) > 1 :
    print(s[-1] - s[0])
else :
    print(0)