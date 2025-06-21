# 설탕 배달
# 그리디 알고리즘 공부 필요

n = int(input())

# 5킬로 그람으로 다 끝낼 수 있으면 바로 정답
if n % 5 == 0 :
    print(n // 5)
    quit()

count = 0
remain = 0
max_num = n // 5

for i in range(max_num,0,-1) :
    r = n - (i * 5) 
    
    if r % 3 == 0 :
        count += i + (r // 3)
        break

if not count :
    q,remain = divmod(n, 3)
    
    if remain :
        count = -1
    else :
        count = q
    
print(count)