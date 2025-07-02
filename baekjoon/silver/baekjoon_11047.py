# 동전
# 그리디 알고리즘? 왜? 인지 모르겠지만 그렇다고 한다.

n, price = map(int, input().split())

coin_lst = []
count = 0
for _ in range(n) :
    c = int(input())
    coin_lst.append(c)

coin_lst.reverse()
for coin in coin_lst :
    if coin > price :
        continue
    
    q, r = divmod(price, coin)
    
    count += q
    
    price = r
    
    if price == 0 :
        break
    
print(count)