# 수 찾기

n = int(input())
a = list(map(int,input().split()))
m = int(input())
m_lst = list(map(int,input().split()))

# 같은 원소를 가지고 있더라도 set과 list, tuple 등과는 in 연산자의 속도가 완전히 다르다!!
# i in set -> O(1) 상수 시간
# i in list -> O(n) 시간 걸림!
# 이 차이를 잘 알아두자.
s = set(a)

for i in m_lst :
    if i in s :
        print(1)
    else :
        print(0)