# 약수 구하기

# 두 정수 n과 k를 입력받아 n의 정수 중 k 번째로 작은 수를 출력하라

# n = 6 이고 k가 3이라면 6의 정수 1,2,3,6 중 3이다.

n, k = map(int,input().split())

lst = []

for i in range(1,n+1) :
    if i * i > n :
        break
    
    if n % i != 0 :
        continue
    
    if i == (n // i) :
        lst.append(i)
        break    
    
    lst.append(i)
    lst.append(n//i)
    
lst = sorted(lst,reverse=False)

if k <= len(lst) :
    print(lst[k-1])
else :
    print(0)