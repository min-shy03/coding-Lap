# 치킨 쿠폰

def solution(chicken):
    service = 0
    coupon = 0 
    
    while chicken // 10 >= 1 :
        q, r = divmod(chicken, 10)
        chicken = q
        service += q
        coupon += r
    
    coupon += chicken
    chicken = 0
    
    while coupon // 10 >= 1 :
        service += (coupon // 10)
        coupon -= (coupon // 10) * 10 - (coupon // 10)
        
    return service

print(solution(100))