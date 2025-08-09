# 패션왕 신해빈

t = int(input())

for _ in range(t) :
    n = int(input())
    
    d = {}
    
    key = d.keys()
    
    total = 1
    for i in range(n) :
        name, cloth = input().split()
        
        if cloth in key :
            d[cloth] += 1
        else :
            d[cloth] = 1
    
    for k in d.values() :
        total *= (k + 1)
        
    print(total - 1)