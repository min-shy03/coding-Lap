# 듣보잡

n, m = map(int,input().split())

d = {}

keys = d.keys()
for _ in range(n) :
    name = input()
    
    if name in keys :
        d[name] += 1
    else :
        d[name] = 1

for _ in range(m) :
    name = input()
    
    if name in keys :
        d[name] += 1
    else :
        d[name] = 1

# 어차피 중복 없다고 했으니 set으로 실행 시간 단축
lst = set()
for key, val in d.items() :
    if val == 2 :
       lst.add(key)
lst = sorted(lst)

print(len(lst))
for i in lst :
    print(i)