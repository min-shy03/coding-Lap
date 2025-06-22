# 벌집

n = int(input())

num = 1

count = 0

while True :
    if n <= num:
        if n == 1 :
            count += 1
        break

    num += 6 * count  
    
    count += 1
    
print(count)