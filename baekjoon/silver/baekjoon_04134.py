# 다음 소수

count = int(input())

for _ in range(count) :
    n = int(input())
    
    if n == 0 or n == 1 :
        print(2)
        continue
    while True :
        flag = False
        for i in range(2,int(n ** 0.5) + 1) :
            if n % i == 0 :
                flag = True
                break
        
        if flag :
            n += 1
        else :
            break
        
    print(n)